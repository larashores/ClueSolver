#pragma once

#include <string>


class Player {
public:
    Player(const std::string& name, int num_cards);
    
    explicit operator std::string() const;

    std::string name;
    int num_cards;
};