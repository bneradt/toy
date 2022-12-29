#include "square.h"
#include "occupant.h"

#include <cassert>
#include <stdexcept>
#include <string>

Square::Square() = default;

Square::Square(Occupant *occupant)
{
  if (occupant != nullptr) {
    occupants_.push_back(occupant);
  }
}

void
Square::set_north_neighbor(Square* north_neighbor) {
  north_neighbor_ = north_neighbor;
}

Square*
Square::get_north_neighbor() {
  return north_neighbor_;
}

Square*
Square::get_next_nonwall_north_square() {
  Square *north_square = north_neighbor_;
  while (north_square != nullptr && north_square->is_wall()) {
    north_square = north_square->get_north_neighbor();
  }
  return north_square;
}

void
Square::set_south_neighbor(Square* south_neighbor) {
  south_neighbor_ = south_neighbor;
}

Square*
Square::get_south_neighbor() {
  return south_neighbor_;
}

Square*
Square::get_next_nonwall_south_square() {
  Square *south_square = south_neighbor_;
  while (south_square != nullptr && south_square->is_wall()) {
    south_square = south_square->get_south_neighbor();
  }
  return south_square;
}

void
Square::set_west_neighbor(Square* west_neighbor) {
  west_neighbor_ = west_neighbor;
}

Square*
Square::get_west_neighbor() {
  return west_neighbor_;
}

Square*
Square::get_next_nonwall_west_square() {
  Square *west_square = west_neighbor_;
  while (west_square != nullptr && west_square->is_wall()) {
    west_square = west_square->get_west_neighbor();
  }
  return west_square;
}

void
Square::set_east_neighbor(Square* east_neighbor) {
  east_neighbor_ = east_neighbor;
}

Square*
Square::get_east_neighbor() {
  return east_neighbor_;
}

Square*
Square::get_next_nonwall_east_square() {
  Square *east_square = east_neighbor_;
  while (east_square != nullptr && east_square->is_wall()) {
    east_square = east_square->get_east_neighbor();
  }
  return east_square;
}

void
Square::add_occupant(Occupant *occupant)
{
  if (occupants_.size() > 2) {
    // We never expect to need more than 3 occupants in a square.
    std::string message = "Cannot add more than three occupants to a square.";
    throw std::invalid_argument(message);
  }
  // Something is wrong if the occupant is already in the square.
  if (std::find(occupants_.begin(), occupants_.end(), occupant) !=
      occupants_.end()) {
    std::string message =
      "Cannot add an occupant to a square that already has that occupant.";
    throw std::logic_error(message);
  }
  occupants_.push_back(occupant);
}

void
Square::remove_occupant(Occupant *occupant)
{
  if (occupant == nullptr) {
    std::string message = "Cannot remove an empty occupant from a square.";
    throw std::invalid_argument(message);
  }
  auto it = std::find(occupants_.begin(), occupants_.end(), occupant);
  if (it == occupants_.end()) {
    std::string message = "Cannot remove an occupant that is not present: ";
    message += occupant->get_string();
    throw std::runtime_error(message);
  }
  occupants_.erase(it);
}

bool
Square::is_empty() const
{
  return occupants_.size() == 0;
}

bool
Square::is_empty_except_for_expediton() const
{
  return occupants_.size() == 1 && occupants_[0]->is_expedition();
}

bool
Square::is_wall() const
{
  auto const it = std::find_if(occupants_.begin(), occupants_.end(),
                                     [](Occupant *occupant) {
                                       return occupant->is_wall();
                                     });
  auto const has_wall = it != occupants_.end();
  if (has_wall) {
    if (occupants_.size() != 1) {
      throw std::logic_error("A wall square should have no other occupants.");
    }
    return true;
  }
  return false;
}

bool
Square::has_expedition() const
{
  auto const it = std::find_if(occupants_.begin(), occupants_.end(),
                                     [](Occupant *occupant) {
                                       return occupant->is_expedition();
                                     });
  return it != occupants_.end();
}

int
Square::get_number_of_occupants() const
{
  return occupants_.size();
}

std::string
Square::get_string() const
{
  auto const number_of_occupants = occupants_.size();
  if (number_of_occupants == 0) {
    return ".";
  }
  if (number_of_occupants > 1) {
    return std::to_string(number_of_occupants);
  }

  auto const& occupant = occupants_[0];
  return occupant->get_string();
}
