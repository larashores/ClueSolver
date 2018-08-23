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

    void add_override(Game& game, const Player* player, const Card* card, bool yes)
    {
        if(yes)
        {
            game.positive_overrides[player].push_back(card);
        } else
        {
            game.negative_overrides[player].push_back(card);
        }
    }

    PY::dict positive_overrides(Game& game)
    {
        boost::python::dict dict;
        for(auto& [player, cards]: game.positive_overrides)
        {
            boost::python::list list;
            for(auto& card: cards)
            {
                list.append(std::shared_ptr<const Card>(card, [=](auto){}));
            }
            dict[std::shared_ptr<const Player>(player, [=](auto){})] = list;
        }
        return dict;
    }

    PY::dict negative_overrides(Game& game)
    {
        boost::python::dict dict;
        for(auto& [player, cards]: game.negative_overrides)
        {
            boost::python::list list;
            for(auto& card: cards)
            {
                list.append(std::shared_ptr<const Card>(card, [=](auto){}));
            }
            dict[std::shared_ptr<const Player>(player, [=](auto){})] = list;
        }
        return dict;
    }

}  // namespace python