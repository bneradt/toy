#include "occupant.h"
#include "square.h"

#include <stdexcept>
#include <string>

std::unique_ptr<Occupant>
Occupant::occupant_factory(char c, Square *square)
{
  switch(c) {
    case '.':
      return nullptr;
    case 'E':
      return std::make_unique<Expedition>(square);
    case '#':
      return std::make_unique<Wall>(square);
    case '^':
      return std::make_unique<NorthBlowingBlizzard>(square);
    case 'v':
      return std::make_unique<SouthBlowingBlizzard>(square);
    case '<':
      return std::make_unique<WestBlowingBlizzard>(square);
    case '>':
      return std::make_unique<EastBlowingBlizzard>(square);
    default:
      std::string message = "Invalid character: ";
      message += c;
      throw std::invalid_argument(message);
  }

  // Not reachable.
  return nullptr;
}

Occupant::Occupant(Square *square) : square(square) {}

void
Occupant::advance()
{
}

void
Occupant::reverse()
{
}

bool
Occupant::is_wall() const
{
  return false;
}

bool
Occupant::is_blizzard() const
{
  return false;
}

bool
Occupant::is_expedition() const
{
  return false;
}

Wall::Wall(Square *square) : Occupant(square) {}

bool
Wall::is_wall() const
{
  return true;
}

std::string
Wall::get_string() const
{
  return "#";
}

Expedition::Expedition(Square *square) : Occupant(square) {}

bool
Expedition::is_expedition() const
{
  return true;
}

std::string
Expedition::get_string() const
{
  return "E";
}

NorthBlowingBlizzard::NorthBlowingBlizzard(Square *square) : Occupant(square) {}

bool
NorthBlowingBlizzard::is_blizzard() const
{
  return true;
}

std::string
NorthBlowingBlizzard::get_string() const
{
  return "^";
}

void
NorthBlowingBlizzard::advance()
{
  Square *north_square = square->get_next_nonwall_north_square();
  square->remove_occupant(this);
  north_square->add_occupant(this);
  square = north_square;
}

void
NorthBlowingBlizzard::reverse()
{
  Square *south_square = square->get_next_nonwall_south_square();
  square->remove_occupant(this);
  south_square->add_occupant(this);
  square = south_square;
}

SouthBlowingBlizzard::SouthBlowingBlizzard(Square *square) : Occupant(square) {}

bool
SouthBlowingBlizzard::is_blizzard() const
{
  return true;
}

std::string
SouthBlowingBlizzard::get_string() const
{
  return "v";
}

void
SouthBlowingBlizzard::advance()
{
  Square *south_square = square->get_next_nonwall_south_square();
  square->remove_occupant(this);
  south_square->add_occupant(this);
  square = south_square;
}

void
SouthBlowingBlizzard::reverse()
{
  Square *north_square = square->get_next_nonwall_north_square();
  square->remove_occupant(this);
  north_square->add_occupant(this);
  square = north_square;
}

EastBlowingBlizzard::EastBlowingBlizzard(Square *square) : Occupant(square) {}

bool
EastBlowingBlizzard::is_blizzard() const
{
  return true;
}

std::string
EastBlowingBlizzard::get_string() const
{
  return ">";
}

void
EastBlowingBlizzard::advance()
{
  Square *east_square = square->get_next_nonwall_east_square();
  square->remove_occupant(this);
  east_square->add_occupant(this);
  square = east_square;
}

void
EastBlowingBlizzard::reverse()
{
  Square *west_square = square->get_next_nonwall_west_square();
  square->remove_occupant(this);
  west_square->add_occupant(this);
  square = west_square;
}

WestBlowingBlizzard::WestBlowingBlizzard(Square *square) : Occupant(square) {}

bool
WestBlowingBlizzard::is_blizzard() const
{
  return true;
}

std::string
WestBlowingBlizzard::get_string() const
{
  return "<";
}

void
WestBlowingBlizzard::advance()
{
  Square *west_square = square->get_next_nonwall_west_square();
  square->remove_occupant(this);
  west_square->add_occupant(this);
  square = west_square;
}

void
WestBlowingBlizzard::reverse()
{
  Square *east_square = square->get_next_nonwall_east_square();
  square->remove_occupant(this);
  east_square->add_occupant(this);
  square = east_square;
}
