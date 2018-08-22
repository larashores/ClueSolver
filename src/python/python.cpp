#include <boost/python.hpp>
#include <boost/python/return_internal_reference.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>
#include <boost/python/register_ptr_to_python.hpp>

#include "python/cards/py_cards.h"
#include "python/cards/py_deck.h"
#include "python/py_player.h"
#include "python/py_guess.h"
#include "python/py_stats.h"
#include "python/py_analyzer.h"
#include "python/py_game.h"

#include "cards/card.h"
#include "cards/person.h"
#include "cards/weapon.h"
#include "cards/room.h"
#include "cards/deck.h"
#include "player.h"
#include "guess.h"
#include "stats.h"
#include "analyzer.h"
#include "game.h"

namespace PY = boost::python;

BOOST_PYTHON_MODULE(pyclue)
{
    PY::enum_<Card::CardType>("CardType")
            .value("PERSON", Card::PERSON)
            .value("WEAPON", Card::WEAPON)
            .value("ROOM", Card::ROOM);

    PY::class_<Card>("Card", PY::no_init)
            .def_readonly("name", &Card::name)
            .def_readonly("type", &Card::type)
            .def(PY::self_ns::str(PY::self_ns::self));

    PY::class_<Person, PY::bases<Card>>("Person", PY::init<const std::string&>());
    PY::class_<Weapon, PY::bases<Card>>("Weapon", PY::init<const std::string&>());
    PY::class_<Room, PY::bases<Card>>("Room", PY::init<const std::string&>());
    PY::register_ptr_to_python<std::shared_ptr<Person>>();
    PY::register_ptr_to_python<std::shared_ptr<Weapon>>();
    PY::register_ptr_to_python<std::shared_ptr<Room>>();
    PY::register_ptr_to_python<std::shared_ptr<const Person>>();
    PY::register_ptr_to_python<std::shared_ptr<const Weapon>>();
    PY::register_ptr_to_python<std::shared_ptr<const Room>>();

    PY::class_<Deck>("Deck")
            .def("people", &python::people)
            .def("weapons", &python::weapons)
            .def("rooms", &python::rooms);

    PY::class_<Player, boost::noncopyable>("Player", PY::init<const std::string&, int>())
            .def_readwrite("name", &Player::name)
            .def_readwrite("num_cards", &Player::num_cards)
            .def(PY::self_ns::str(PY::self_ns::self));
    PY::register_ptr_to_python<std::shared_ptr<Player>>();

    PY::class_<Guess, boost::noncopyable>("Guess", PY::no_init)
            .def("guesser", &python::guesser, PY::return_internal_reference<>())
            .def("answerer", &python::answerer, PY::return_internal_reference<>())
            .def("murderer", &python::murderer, PY::return_internal_reference<>())
            .def("weapon", &python::weapon, PY::return_internal_reference<>())
            .def("room", &python::room, PY::return_internal_reference<>())
            .def("answer", &python::answer, PY::return_internal_reference<>());

    PY::class_<Stats, boost::noncopyable>("Stats")
            .def("positives", &python::positives)
            .def("negatives", &python::negatives);

    PY::class_<Game, boost::noncopyable>("Game")
            .def("add_player", &Game::add_player)
            .def("add_guess", &Game::add_guess)
            .def("add_override", &Game::add_override)
            .def("get_guesses", &python::get_guesses)
            .def("get_players", &python::get_players)
            .def("remaining_cards", &Game::get_remaining_cards)
            .def("set_active_player", &Game::set_active_player)
            .def("active_player", &Game::get_active_player, PY::return_internal_reference<>())
            .def_readonly("deck", &Game::deck)
            .def_readonly("analyzer", &Game::analyzer);

    PY::class_<Analyzer>("Analyzer", PY::init<const Game&>())
            .def("stats", &python::get_stats);
}
