#include "python/py_game.h"

#include "override.h"

namespace PY = boost::python;

namespace python {

    PY::list get_guesses(Game& game)
    {
        boost::python::list list;
        for(auto& guess: game.get_guesses())
        {
            list.append(std::shared_ptr<Guess>(&guess, [=](void*){}));
        }
        return list;
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

    PY::dict overrides(Game& game)
    {
        boost::python::dict dict;
        for(auto& [player, card_map]: game.overrides)
        {
            boost::python::list list;
            for(auto& [card, override_type]: card_map)
            {
                list.append(PY::make_tuple(std::shared_ptr<const Card>(card, [=](auto){}),
                                           override_type == Override::POSITIVE));
            }
            dict[std::shared_ptr<const Player>(player, [=](auto){})] = list;
        }
        return dict;
    }

    void clear_overrides(Game& game)
    {
        game.overrides.clear();
    }

    void add_guess(Game& game, const Player& guessor, const Player* answerer, PY::list skipped,
                   const Person& murderer, const Weapon& weapon, const Room& room,
                   const Card* card)
    {
        std::vector<Player*> dont_haves;
        for (int i = 0; i < PY::len(skipped); i++)
        {
            dont_haves.push_back(PY::extract<Player*>(skipped[i]));
        }
        game.add_guess(guessor, answerer, dont_haves, murderer, weapon, room, card);
    }
}  // namespace python