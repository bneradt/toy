#pragma once

#include <vector>

/** A representation of a set of supply stacks.
 *
 * An object of this type is assumed to be initialized through a series of
 * add_crate calls followed by a series of move_crate calls.
 */
class SupplyStacks
{
public:
  /** Whether the updated mover should be used.
   *
   * If this is true, then the crate mover is configured with the ability to
   * move multiple stacks at once rather than one at a time.
   */
  static constexpr bool USE_UPDATED_MOVER = true;

  SupplyStacks(bool use_updated_mover);

  /** Add a crate to one of the stacks.
   *
   * @param[in] stack_id The stack to add the crate to. This is one-indexed.
   * @param[in] crate_name The name of the crate to add.
   */
  void add_crate(size_t stack_id, char crate_name);

  /** Move @a num_crates crates from @a from_stack to @a to_stack.
   *
   * @param[in] num_crates The number of crates to move.
   * @param[in] from_stack The stack to move crates from.
   * @param[in] to_stack The stack to move crates to.
   */
  void move_crate(int num_crates, int from_stack, int to_stack);

  /** Retrieve the top crate from each stack.
   *
   * @return A vector containing the top crate from each stack.
   */
  std::vector<char> get_stack_tops();

private:
  /** Reverse the order of the stacks.
   *
   * The stacks are added in top down order. To manipulate them, we need to
   * access them in reverse order. That is, the crane manipulates the stacks as
   * a LIFO. Presently they are added such that the top-most is at the "front"
   * of the std::vector, but that's the one we need to move first.
   */
  void reverse_stacks();

private:
  /** Whether the mover has the ability to move multiple crates at once. */
  bool use_updated_mover_;

  using Stack  = std::vector<char>;
  using Stacks = std::vector<Stack>;
  Stacks stacks_;

  bool stacks_are_reversed_ = false;
};
