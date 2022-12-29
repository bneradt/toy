#pragma once

#include <memory>
#include <string>

class Square;

class Occupant {
public:
  /** Interprets a character and returns an appropriate Occupant.
   *
   * @param[in] c the character to interpret.
   *
   * @param[in] square The square the occupant starts out on.
   *
   * @return the Occupant corresponding to the character.
   *
   * @throws std::invalid_argument if the character is not correlated with a
   * valid Occupant.
   */
  static std::unique_ptr<Occupant> occupant_factory(char c, Square *square);

  /** Construct an occupant.
   *
   * @param[in] square The square that the occupant is on.
   */
  Occupant(Square* square);

  virtual ~Occupant() = default;

  /** The occupant is a wall.
   *
   * @return true if the occupant is a wall, false otherwise.
   */
  virtual bool is_wall() const;

  /** The occupant is a blizzard.
   *
   * @return true if the occupant is a blizzard, false otherwise.
   */
  virtual bool is_blizzard() const;

  /** The occupant is the expedition.
   *
   * @return true if the occupant is the expedition, false otherwise.
   */
  virtual bool is_expedition() const;

  /** Return a string representation of the occupant.
   *
   * @return a string representation of the occupant.
   */
  virtual std::string get_string() const = 0;

  /** Have the occupant move one unit, if it is non-stationary.
   */
  virtual void advance();

  /** Have the occupant revert back one square, if it is non-stationary.
   */
  virtual void reverse();

protected:
  /** The square the occupant is on. */
  Square *square;
};

class Wall : public Occupant {
public:
  /** Construct a Wall.
   *
   * @param[in] square The square the wall starts out on.
   */
  Wall(Square *square);

  /** The occupant is a wall.
   *
   * @return true if the occupant is a wall, false otherwise.
   */
  bool is_wall() const override;

  /** Returns a string representation of the wall.
   *
   * @return a string representation of the wall.
   */
  std::string get_string() const override;
};

class Expedition : public Occupant {
public:
  /** Construct an Expedition.
   *
   * @param[in] square The square the expedition starts out on.
   */
  Expedition(Square *square);

  /** The occupant is the expedition.
   *
   * @return true if the occupant is the expedition, false otherwise.
   */
  bool is_expedition() const override;

  /** Returns a string representation of the expedition.
   *
   * @return a string representation of the expedition.
   */
  std::string get_string() const override;
};

class NorthBlowingBlizzard : public Occupant {
public:
  /** Construct a NorthBlowingBlizzard.
   *
   * @param[in] square The square the blizzard starts out on.
   */
  NorthBlowingBlizzard(Square *square);

  /** The occupant is a blizzard.
   *
   * @return true if the occupant is a blizzard, false otherwise.
   */
  bool is_blizzard() const override;

  /** Returns a string representation of the blizzard.
   *
   * @return a string representation of the blizzard.
   */
  std::string get_string() const override;

  /** Have the blizzard advance one square north.
   */
  void advance() override;

  /** Have the blizzard reverse one square south.
   */
  void reverse() override;
};

class SouthBlowingBlizzard : public Occupant {
public:
  /** Construct a SouthBlowingBlizzard.
   *
   * @param[in] square The square the blizzard starts out on.
   */
  SouthBlowingBlizzard(Square *square);

  /** The occupant is a blizzard.
   *
   * @return true if the occupant is a blizzard, false otherwise.
   */
  bool is_blizzard() const override;

  /** Returns a string representation of the blizzard.
   *
   * @return a string representation of the blizzard.
   */
  std::string get_string() const override;

  /** Have the blizzard advance one square south.
   */
  void advance() override;

  /** Have the blizzard reverse one square north.
   */
  void reverse() override;
};

class EastBlowingBlizzard : public Occupant {
public:
  /** Construct a EastBlowingBlizzard.
   *
   * @param[in] square The square the blizzard starts out on.
   */
  EastBlowingBlizzard(Square *square);

  /** The occupant is a blizzard.
   *
   * @return true if the occupant is a blizzard, false otherwise.
   */
  bool is_blizzard() const override;

  /** Returns a string representation of the blizzard.
   *
   * @return a string representation of the blizzard.
   */
  std::string get_string() const override;

  /** Have the blizzard advance one square east.
   */
  void advance() override;

  /** Have the blizzard reverse one square west.
   */
  void reverse() override;
};

class WestBlowingBlizzard : public Occupant {
public:
  /** Construct a WestBlowingBlizzard.
   *
   * @param[in] square The square the blizzard starts out on.
   */
  WestBlowingBlizzard(Square *square);

  /** The occupant is a blizzard.
   *
   * @return true if the occupant is a blizzard, false otherwise.
   */
  bool is_blizzard() const override;

  /** Returns a string representation of the blizzard.
   *
   * @return a string representation of the blizzard.
   */
  std::string get_string() const override;

  /** Have the blizzard advance one square west.
   */
  void advance() override;

  /** Have the blizzard reverse one square east.
   */
  void reverse() override;
};
