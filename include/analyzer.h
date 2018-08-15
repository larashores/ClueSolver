#pragma once

#include <map>

#include "player.h"
#include "stats.h"

class Game;


class Analyzer
{
public:
    explicit Analyzer(const Game& game);

    std::map<const Player*, Stats> get_stats() const;

private:
    void analyze_negatives(std::map<const Player *, Stats>& stats) const;
    const Game& m_game;
};
