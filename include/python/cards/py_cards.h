#pragma once

#include <iostream>

#include "cards/card.h"

std::ostream& operator<<(std::ostream& stream, const Card& card);
bool operator==(const Card& card1, const Card& card2);


namespace python {

long hash_card(const Card& card);

}  // namespace python
