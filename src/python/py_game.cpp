#include "python/py_game.h"

namespace PY = boost::python;

namespace python {

    PY::list get_guesses(Game& game)
    {
        return stl2pyptr(game.get_guesses());
    }

    PY::list get_players(Game& game)
    {
        boost::python::list list;
        for(auto& player: game.get_players())
        {
            list.append(std::shared_ptr<Player>(player, [=](void*){}));
        }
        return list;
    }

}  // namespace python