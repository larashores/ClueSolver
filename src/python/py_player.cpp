#include <iostream>

#include <boost/python.hpp>

#include <sstream>

#include "python/py_player.h"

std::ostream& operator<<(std::ostream& stream, const Player& player)
{
    return stream << std::string{player};
}