#include "valley.h"
#include "occupant.h"

#include <stdexcept>
#include <string>

Valley::Valley()
{
  rows_.emplace_back();
}

void
Valley::add_square(char c)
{
  auto &last_row = rows_.back();
  auto& new_square = last_row.emplace_back();
  std::unique_ptr<Occupant> occupant = Occupant::occupant_factory(c, &new_square);
  if (!occupant) {
    return;
  }

  if (occupant->is_expedition()) {
    expedition_coordinates_ = std::make_pair(rows_.size() - 1, last_row.size() - 1);

    if (expedition_) {
      throw std::invalid_argument("Cannot add more than one expedition.");
    }
    expedition_ = occupant.get();
  }

  new_square.add_occupant(occupant.get());
  occupants_.push_back(std::move(occupant));
}

void
Valley::start_new_row()
{
  rows_.emplace_back();
}

void
Valley::set_neighbors()
{
  for (size_t row = 0; row < rows_.size(); ++row) {
    for (size_t col = 0; col < rows_[row].size(); ++col) {
      auto* square = &rows_[row][col];

      Square *north = nullptr;
      if (row > 0) {
        north = &rows_[row - 1][col];
      } else {
        north = &rows_[rows_.size() - 1][col];
      }
      square->set_north_neighbor(north);

      Square *south = nullptr;
      if (row < rows_.size() - 1) {
        south = &rows_[row + 1][col];
      } else {
        south = &rows_[0][col];
      }
      square->set_south_neighbor(south);

      Square *west = nullptr;
      if (col > 0) {
        west = &rows_[row][col - 1];
      } else {
        west = &rows_[row][rows_[row].size() - 1];
      }
      square->set_west_neighbor(west);

      Square *east = nullptr;
      if (col < rows_[row].size() - 1) {
        east = &rows_[row][col + 1];
      } else {
        east = &rows_[row][0];
      }
      square->set_east_neighbor(east);
    }
  }
  neighbors_are_set_ = true;
}

std::string
Valley::get_string() const
{
  std::string representation;
  representation.reserve(rows_.size() * rows_.front().size() + rows_.size());
  for (const auto& row : rows_) {
    for (const auto& square : row) {
      representation += square.get_string();
    }
    representation += "\n";
  }
  return representation;
}

std::pair<int, int>
Valley::get_expedition_coordinates() const
{
  return expedition_coordinates_;
}

void
Valley::advance_weather_one_minute()
{
  if (!neighbors_are_set_) {
    throw std::runtime_error("Cannot advance weather without setting neighbors.");
  }
  for (auto& occupant : occupants_) {
    occupant->advance();
  }
}

void
Valley::reverse_weather_one_minute()
{
  if (!neighbors_are_set_) {
    throw std::runtime_error("Cannot advance weather without setting neighbors.");
  }
  for (auto& occupant : occupants_) {
    occupant->reverse();
  }
}

void
Valley::move_expedition_south()
{
  if (!neighbors_are_set_) {
    throw std::runtime_error("Cannot advance weather without setting neighbors.");
  }
  auto const current_row = expedition_coordinates_.first;
  auto const current_column = expedition_coordinates_.second;

  if (current_row == rows_.size() - 1) {
    throw std::out_of_range("Cannot move expedition below the edge of the map.");
  }

  auto& destination_square = rows_[current_row + 1][current_column];
  if (!destination_square.is_empty()) {
    throw std::runtime_error("Expedition cannot move to the non-empty square.");
  }
  auto& current_square = rows_[current_row][current_column];
  if (!current_square.has_expedition()) {
    throw std::logic_error("Expedition source square does not have the expedition in it.");
  }

  current_square.remove_occupant(expedition_);
  destination_square.add_occupant(expedition_);
  expedition_coordinates_.first++;
}

void
Valley::move_expedition_north()
{
  if (!neighbors_are_set_) {
    throw std::runtime_error("Cannot advance weather without setting neighbors.");
  }
  auto const current_row = expedition_coordinates_.first;
  auto const current_column = expedition_coordinates_.second;

  if (current_row == 0) {
    throw std::out_of_range("Cannot move expedition above the edge of the map.");
  }

  auto& destination_square = rows_[current_row - 1][current_column];
  if (!destination_square.is_empty()) {
    throw std::runtime_error("Expedition cannot move to the non-empty square.");
  }
  auto& current_square = rows_[current_row][current_column];
  if (!current_square.has_expedition()) {
    throw std::logic_error("Expedition source square does not have the expedition in it.");
  }

  current_square.remove_occupant(expedition_);
  destination_square.add_occupant(expedition_);
  expedition_coordinates_.first--;
}

void
Valley::move_expedition_east()
{
  if (!neighbors_are_set_) {
    throw std::runtime_error("Cannot advance weather without setting neighbors.");
  }
  auto const current_row = expedition_coordinates_.first;
  auto const current_column = expedition_coordinates_.second;

  if (current_column == rows_[current_row].size() - 1) {
    throw std::out_of_range("Cannot move expedition to the right of the edge of the map.");
  }

  auto& destination_square = rows_[current_row][current_column + 1];
  if (!destination_square.is_empty()) {
    throw std::runtime_error("Expedition cannot move to the non-empty square.");
  }
  auto& current_square = rows_[current_row][current_column];
  if (!current_square.has_expedition()) {
    throw std::logic_error("Expedition source square does not have the expedition in it.");
  }

  current_square.remove_occupant(expedition_);
  destination_square.add_occupant(expedition_);
  expedition_coordinates_.second++;
}

void
Valley::move_expedition_west()
{
  if (!neighbors_are_set_) {
    throw std::runtime_error("Cannot advance weather without setting neighbors.");
  }
  auto const current_row = expedition_coordinates_.first;
  auto const current_column = expedition_coordinates_.second;

  if (current_column == 0) {
    throw std::out_of_range("Cannot move expedition to the left of the edge of the map.");
  }

  auto& destination_square = rows_[current_row][current_column - 1];
  if (!destination_square.is_empty()) {
    throw std::runtime_error("Expedition cannot move to the non-empty square.");
  }
  auto& current_square = rows_[current_row][current_column];
  if (!current_square.has_expedition()) {
    throw std::logic_error("Expedition source square does not have the expedition in it.");
  }

  current_square.remove_occupant(expedition_);
  destination_square.add_occupant(expedition_);
  expedition_coordinates_.second--;
}
