cmake_minimum_required(VERSION 3.12)
project(hello VERSION 1.0)
 
#-----------Project Files------------
set(SOURCE_FILES src/game.cpp
                 src/player.cpp
                 src/guess.cpp
                 src/utilities.cpp
                 src/cards/card.cpp
                 src/cards/deck.cpp
                 src/cards/person.cpp
                 src/cards/weapon.cpp
                 src/cards/room.cpp
                 src/analyzer.cpp)
set(TEST_SOURCE_FILES src/main.cpp)
set(LIB_SOURCE_FILES src/python/python.cpp
                     src/python/cards/py_cards.cpp
                     src/python/cards/py_deck.cpp
                     src/python/py_guess.cpp
                     src/python/py_player.cpp
                     src/python/py_stats.cpp
                     src/python/py_utilities.cpp
                     src/python/py_analyzer.cpp
                     src/python/py_game.cpp)

set(HEADER_FILES include/game.h
                 include/player.h
                 include/guess.h
                 include/utilities.h
                 include/stats.h
                 include/cards/card.h
                 include/cards/deck.h
                 include/cards/person.h
                 include/cards/weapon.h
                 include/cards/room.h
                 include/analyzer.h)
set(LIB_HEADER_FILES include/python/cards/py_cards.h
                     include/python/cards/py_deck.h
                     include/python/py_guess.h
                     include/python/py_player.h
                     include/python/py_stats.h
                     include/python/py_utilities.h
                     include/python/py_analyzer.h
                     include/python/py_game.h)

#------------------------------------
 
#-----------Build options------------
set(ARCHITECTURE x64)
set(BUILD_STATIC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++17 -Wall -Wextra -pedantic -g")
set(CMAKE_CXX_COMPILER_ARCHITECTURE_ID ${ARCHITECTURE})  # Used to find Boost libraries correctly
#------------------------------------

#------Find boost python library-----
set(BOOST_LIBRARYDIR C:/boost_1_67_0/stage/${ARCHITECTURE}/lib)
set(Boost_USE_STATIC_LIBS ${BUILD_STATIC})
set(Boost_USE_MULTITHREADED ON)
set(Boost_USE_STATIC_RUNTIME ${BUILD_STATIC})
if(${BUILD_STATIC})
    add_definitions(-DBOOST_PYTHON_STATIC_LIB)
endif()
find_package(Boost 1.67.0 REQUIRED python37)
if (Boost_FOUND)
    message(" Boost include directory found at ${Boost_INCLUDE_DIRS}")
    message(" Boost libraries found at ${Boost_LIBRARIES}")
else()
    message(" Boost not found")
    return()
endif()
#-----------------------------------
    
#-----Find python link library------
find_package(PythonLibs 3.7 REQUIRED)
if (PYTHONLIBS_FOUND)
    message(" Python include directory found at ${PYTHON_INCLUDE_DIRS}")
    message(" Python libraries found at ${PYTHON_LIBRARIES}")
else()
    message(" Python not found")
endif()
#-----------------------------------

#----------Add Test C++ Main--------
add_executable(Clue ${SOURCE_FILES} ${TEST_SOURCE_FILES} ${HEADER_FILES})
target_include_directories(Clue PRIVATE include)
#-----------------------------------

#---------Add Python Library--------
add_library(pyclue MODULE ${SOURCE_FILES} ${LIB_SOURCE_FILES} ${HEADER_FILES} ${LIB_HEADER_FILES})
set_target_properties(pyclue PROPERTIES PREFIX "")
set_target_properties(pyclue PROPERTIES SUFFIX ".pyd")
target_include_directories(pyclue PRIVATE include)

target_include_directories(pyclue SYSTEM PRIVATE ${Boost_INCLUDE_DIRS} ${PYTHON_INCLUDE_DIRS})
target_link_libraries(pyclue ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
#-----------------------------------