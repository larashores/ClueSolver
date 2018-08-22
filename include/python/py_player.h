#pragma once

#include <iostream>

#include "player.h"

std::ostream& operator<<(std::ostream& stream, const Player& player);
bool operator==(const Player& player1, const Player& player2);