#pragma once

#include <boost/python.hpp>
#include "cards/person.h"

namespace python {

template<typename Sequence>
boost::python::list stl2py(const Sequence& sequence)
{
    boost::python::list list;
    for(auto& arg: sequence)
    {
        list.append(arg);
    }
    return list;
}

template<typename Sequence>
boost::python::list stl2pyptr(Sequence sequence)
{
    boost::python::list list;
    for(auto& arg: sequence)
    {
        list.append(&arg);
    }
    return list;
}

template <typename T, typename std::enable_if_t<!std::is_pointer<T>::value>* = nullptr>
std::shared_ptr<T> to_shared_ptr(T val)
{
    return std::shared_ptr<T>(&val, [=](void*){});
}

template <typename T, typename std::enable_if_t<std::is_pointer<T>::value>* = nullptr>
std::shared_ptr<T> to_shared_ptr(T val)
{
    return std::shared_ptr<T>(val, [=](void*){});
}

template<typename Sequence>
boost::python::list to_ptr_list(Sequence sequence)
{
    boost::python::list list;
    for(auto& arg: sequence)
    {
        list.append(to_shared_ptr(arg));
    }
    return list;
}

}  // namespace