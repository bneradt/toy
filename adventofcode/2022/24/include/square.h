#pragma once

#include <string>
#include <vector>

class Occupant;

/** Represents a square in the valley and any of its content.
 *
 * There are a few significant attributes to squares:
 *
 * - Squares have neighbors to the north, south, east, and west.
 * - Boundary squares are walls, with the exception of the entrances to the
 *   valley.
 * - Squares are wrapped in linked-list fashion such that wall squares link to
 *   the wall on the other side of the valley.
 */
class Square {
public:
  /** Construct an empty Square. */
  Square();

  /** Constructs a square with the given content.
   *
   * @param[in] occupant The content of the square. If this value is nullptr,
   * the square is empty.
   */
  Square(Occupant *occupant);

  /** Set the neighbor to the north.
   *
   * @param[in] neighbor The neighbor to the north.
   */
  void set_north_neighbor(Square* north_neighbor);

  /** Get the neighbor to the north.
   *
   * @return The neighbor to the north.
   */
  Square* get_north_neighbor();

  /** Get the next neighbor to the north, wrapping to the south if the neighbor
   * to the north is a wall.
   *
   * @return The next non-wall neighbor to the north.
   */
  Square* get_next_nonwall_north_square();

  /** Set the neighbor to the south.
   *
   * @param[in] neighbor The neighbor to the south.
   */
  void set_south_neighbor(Square* south_neighbor);

  /** Get the neighbor to the south.
   *
   * @return The neighbor to the south.
   */
  Square* get_south_neighbor();

  /** Get the next neighbor to the south, wrapping to the north if the neighbor
   * to the south is a wall.
   *
   * @return The next non-wall neighbor to the south.
   */
  Square* get_next_nonwall_south_square();

  /** Set the neighbor to the west.
   *
   * @param[in] neighbor The neighbor to the west.
   */
  void set_west_neighbor(Square* west_neighbor);

  /** Get the neighbor to the west.
   *
   * @return The neighbor to the west.
   */
  Square* get_west_neighbor();

  /** Get the next neighbor to the west, wrapping to the east if the neighbor
   * to the west is a wall.
   *
   * @return The next non-wall neighbor to the west.
   */
  Square* get_next_nonwall_west_square();

  /** Set the neighbor to the east.
   *
   * @param[in] neighbor The neighbor to the east.
   */
  void set_east_neighbor(Square* east_neighbor);

  /** Get the neighbor to the east.
   *
   * @return The neighbor to the east.
   */
  Square* get_east_neighbor();

  /** Get the next neighbor to the east, wrapping to the west if the neighbor
   * to the east is a wall.
   *
   * @return The next non-wall neighbor to the east.
   */
  Square* get_next_nonwall_east_square();

  /** Add the given occupant to the square.
   *
   * @param[in] occupant The occupant to add to the square.
   *
   * @throws std::invalid_argument if the caller attempts to add an occupant to
   * a square that already has three occupants.
   *
   * @throws std::invalid_argument if the caller attempts to add an occupant to
   * a square that already has an occupant of the same type.
   */
  void add_occupant(Occupant* occupant);

  /** Remove the given occupant from the square.
   *
   * @param[in] occupant The occupant to remove from the square.
   *
   * @throws std::runtime_error if the occupant is not in the square.
   *
   * @throws std::invalid_argument if the caller attempts to remove an occupant
   * of type Empty.
   */
  void remove_occupant(Occupant* occupant);

  /** Returns whether the square is empty.
   *
   * @return true if the square has no occupants, false otherwise.
   */
  bool is_empty() const;

  /** Returns whether the only occupant in the squire is the expedition.
   *
   * @return true if the only occupant in the square is the expedition, false
   * otherwise.
   */
  bool is_empty_except_for_expediton() const;

  /** Returns whether the square is a wall.
   *
   * @return true if the square is a wall, false otherwise.
   */
  bool is_wall() const;

  /** Returns whether the square has the expedition in it.
   *
   * @return true if the square has the expedition in it, false otherwise.
   */
  bool has_expedition() const;

  /** Returns the number of occupants in the square.
   *
   * @return the number of occupants in the square.
   */
  int get_number_of_occupants() const;

  /** Returns a string representation of the square.
   *
   * @return A string representation of the square.
   */
  std::string get_string() const;

private:

  /** The content of the square.
   *
   * @note That empty squares have no occupants.
   */
  std::vector<Occupant*> occupants_;

  /** The neighbor to the north. */
  Square *north_neighbor_{nullptr};

  /** The neighbor to the south. */
  Square *south_neighbor_{nullptr};

  /** The neighbor to the west. */
  Square *west_neighbor_{nullptr};

  /** The neighbor to the east. */
  Square *east_neighbor_{nullptr};
};
