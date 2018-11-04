#include "python/py_game.h"

#include "override.h"

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
        game.overrides[player][card] = (yes ? Override::POSITIVE : Override::NEGATIVE);
    }

    PY::dict positive_overrides(Game& game)
    {
        boost::python::dict dict;
        for(auto& [player, card_map]: game.overrides)
        {
            boost::python::list list;
            for(auto& [card, override_type]: card_map)
            {
                if (override_type == Override::POSITIVE)
                {
                    list.append(std::shared_ptr<const Card>(card, [=](auto){}));
                }
            }
            dict[std::shared_ptr<const Player>(player, [=](auto){})] = list;
        }
        return dict;
    }

    PY::dict negative_overrides(Game& game)
    {
        boost::python::dict dict;
        for(auto& [player, card_map]: game.overrides)
        {
            boost::python::list list;
            for(auto& [card, override_type]: card_map)
            {
                if (override_type == Override::NEGATIVE)
                {
                    list.append(std::shared_ptr<const Card>(card, [=](auto){}));
                }
            }
            dict[std::shared_ptr<const Player>(player, [=](auto){})] = list;
        }
        return dict;
    }

}  // namespace python