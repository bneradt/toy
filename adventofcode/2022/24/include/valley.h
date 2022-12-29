#pragma once

#include "occupant.h"
#include "square.h"

#include <memory>
#include <string>
#include <utility>
#include <vector>

class Occupant;

class Valley {
public:

  /** Constructs a valley. */
  Valley();

  /** Add a square to the current row.
   *
   * @param[in] c The character to interpret as an occupant.
   *
   * @throws std::invalid_argument if the character is not correlated with an
   * Occupant instance.
   */
  void add_square(char c);

  /** Start a new row. */
  void start_new_row();

  /** Set the neighbors for each square in the valley.
   */
  void set_neighbors();

  /** Returns a string representation of the valley.
   *
   * @return A string representation of the valley.
   */
  std::string get_string() const;

  /** Advance all the weather patterns one square.
   *
   * @throws std::runtime_error if the @a set_neighbors method has not been
   * called.
   */
  void advance_weather_one_minute();

  /** Reverse all the weather patterns one square.
   *
   * @throws std::runtime_error if the @a set_neighbors method has not been
   * called.
   */
  void reverse_weather_one_minute();

  /** Retrieve the expedition's current coordinates.
   *
   * @return The expedition's current coordinates as (row, column).
   */
  std::pair<int, int> get_expedition_coordinates() const;

  /** Move the expedition north one square.
   *
   * @throws std::runtime_error if the @a set_neighbors method has not been
   * called.
   */
  void move_expedition_north();

  /** Move the expedition south one square.
   *
   * @throws std::runtime_error if the @a set_neighbors method has not been
   * called.
   */
  void move_expedition_south();

  /** Move the expedition west one square.
   *
   * @throws std::runtime_error if the @a set_neighbors method has not been
   * called.
   */
  void move_expedition_west();

  /** Move the expedition east one square.
   *
   * @throws std::runtime_error if the @a set_neighbors method has not been
   * called.
   */
  void move_expedition_east();

private:
  using Row = std::vector<Square>;
  using Grid = std::vector<Row>;

  /** The grid of squares of the valley. */
  Grid rows_;

  /** Whether the neighbors have been set. */
  bool neighbors_are_set_{false};

  /** The expedition's current square. */
  std::pair<size_t, size_t> expedition_coordinates_{0, 0};

  /** The occupants (walls, blizzards, etc.) in the valley. */
  std::vector<std::unique_ptr<Occupant>> occupants_;

  /** The expedition in the valley. */
  Occupant* expedition_{nullptr};
};
