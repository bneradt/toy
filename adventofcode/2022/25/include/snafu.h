#pragma once

#include <cstdint>
#include <string>
#include <string_view>

namespace snafu {

/** Represent a SNAFU number.
 *
 * A SNAFU number is in base 5, where each place represents a power of 5.
 * However, unlike a conventional base 5 system, the values 3 and 4 are removed
 * and replaced with -2 and -1. This means that everywhere where 3 or 4 would
 * be used, the next power has to be used instead and -2 or -1, respectively,
 * has to be used to compensate. Here are the varous digits available:
 *
 * = : -2
 * - : -1
 * 0 :  0
 * 1 :  1
 * 2 :  2
 *
 * Thus:
 * 10 : 5
 * 11 : 6
 * 1=0 : (25 - 10 - 0) = 15
 * 1-0 : (25 - 5 - 0) = 20
 */
class Snafu
{
public:

  enum class Base_t {
    TEN,
    SNAFU,
  };

  // Member functions.
  /** Default constructor.
   *
   * Creates a SNAFU number with a value of 0.
   */
  Snafu();

  /** Construct a Snafu from a decimal value.
   *
   * @param[in] value The decimal value.
   */
  Snafu(int64_t value);

  /** Construct a Snafu from a string representation of a number.
   *
   * @param[in] value The string representing the value.
   *
   * @param[in] base The base of the number.
   */
  Snafu(std::string_view value, Base_t base);

  /** Addition overload for Snafu objects.
   * @param[in] rhs The right hand side of the addition.
   * @return The result of the addition.
   */
  Snafu operator+(Snafu const &rhs) const;

  /** += overload for Snafu objects.
   * @param[in] rhs The right hand side of the addition.
   * @return The result of the addition.
   */
  Snafu &operator+=(Snafu const &rhs);

  /** Subtraction overload for Snafu objects.
   *
   * @note: Snafu is not implemented for negative values.
   *
   * @param[in] rhs The right hand side of the subtraction.
   * @return The result of the subtraction.
   */
  Snafu operator-(Snafu const &rhs) const;

  /** -= overload for Snafu objects.
   *
   * @note: Snafu is not implemented for negative values.
   *
   * @param[in] rhs The right hand side of the subtraction.
   * @return The result of the subtraction.
   */
  Snafu &operator-=(Snafu const &rhs);

  /** Return the decimal value of the number.
   *
   * @return The decimal value.
   */
  int64_t get_decimal() const;

  /** Return the string representation of the number in the SNAFU
   * representation.
   *
   * @return The string representation.
   */
  std::string get_snafu() const;

private:
  /** The decimal value of the number. */
  int64_t decimal_;

  /** The SNAFU representation of the number. */
  std::string snafu_;
};

} // namespace snafu
