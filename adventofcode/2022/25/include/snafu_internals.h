#pragma once

#include <cstdint>
#include <string>
#include <string_view>

/** These functions implement direct SNAFU manipulations. They are used in the
 * internals of the Snafu implementation. */

namespace snafu {

/** Convert a SNAFU number to a decimal number.
 *
 * @param snafu The SNAFU number to convert.
 * @return The decimal value associated with the character.
 */
int convert_snafu_char_to_int(char snafu_char);

/** Convert a SNAFU number to a decimal number.
 *
 * @param[in] snafu The SNAFU number.
 *
 * @return The decimal number.
 */
int64_t convert_snafu_to_decimal(std::string_view snafu);

/** Convert a decimal number to a SNAFU number.
 *
 * @param[in] decimal The decimal number.
 *
 * @return The SNAFU number.
 */
std::string convert_decimal_to_snafu(int64_t decimal);

/** Sum the two snafu values and return the result.
 *
 * @param[in] snafu1 The first SNAFU number.
 * @param[in] snafu2 The second SNAFU number.
 *
 * @return The sum of the two SNAFU numbers.
 */
std::string sum_two_snafus(std::string_view snafu1, std::string_view snafu2);

} // namespace snafu
