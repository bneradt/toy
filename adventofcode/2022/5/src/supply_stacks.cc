#include "supply_stacks.h"

#include <stdexcept>

SupplyStacks::SupplyStacks(bool use_updated_mover)
  : use_updated_mover_{use_updated_mover}
{
}

void
SupplyStacks::add_crate(size_t stack_id, char crate_name)
{
  // The user has to abide by the two phase system: add crates followed by all
  // other API calls. If these get intermixed, then raise an assertion.
  if (stacks_are_reversed_) {
    throw std::runtime_error("Cannot add crates after other API calls");
  }

  // Make sure there are enough stacks for the given stack_id.
  if (stack_id > stacks_.size()) {
    stacks_.resize(stack_id);
  }
  stacks_[stack_id - 1].push_back(crate_name);
}

void
SupplyStacks::move_crate(int num_crates, int from_stack, int to_stack)
{
  // If we are now moving crates, then the addition of crates must be
  // completed.
  if (!stacks_are_reversed_) {
    reverse_stacks();
  }
  if (use_updated_mover_) {
    // The updated mover can move multiple crates at once.
    auto &from = stacks_[from_stack - 1];
    auto &to   = stacks_[to_stack - 1];
    to.insert(to.end(), from.end() - num_crates, from.end());
    from.erase(from.end() - num_crates, from.end());
  } else {
    for (int i = 0; i < num_crates; ++i) {
      stacks_[to_stack - 1].push_back(stacks_[from_stack - 1].back());
      stacks_[from_stack - 1].pop_back();
    }
  }
}

std::vector<char>
SupplyStacks::get_stack_tops()
{
  // We need to make sure that we have arranged the post-initialization phase
  // order.
  if (!stacks_are_reversed_) {
    reverse_stacks();
  }

  std::vector<char> tops;
  for (auto const &stack : stacks_) {
    char top = '\0';
    if (!stack.empty()) {
      top = stack.back();
    }
    tops.push_back(top);
  }
  return tops;
}

void
SupplyStacks::reverse_stacks()
{
  for (auto &stack : stacks_) {
    std::reverse(stack.begin(), stack.end());
  }
  stacks_are_reversed_ = true;
}
