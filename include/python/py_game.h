#pragma once

#include <boost/python.hpp>

#include "python/py_utilities.h"
#include "game.h"

namespace PY = boost::python;

namespace python {
    PY::list get_guesses(Game& game);
    PY::list get_players(Game& game);
    PY::dict overrides(Game& game);
    void add_override(Game& game, const Player* player, const Card* card, bool yes);
    void clear_overrides(Game& game);
}  // namespace python