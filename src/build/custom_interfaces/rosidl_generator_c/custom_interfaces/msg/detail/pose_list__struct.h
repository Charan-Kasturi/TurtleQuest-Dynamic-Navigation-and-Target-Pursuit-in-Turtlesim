// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:msg/PoseList.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__POSE_LIST__STRUCT_H_
#define CUSTOM_INTERFACES__MSG__DETAIL__POSE_LIST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'data'
#include "custom_interfaces/msg/detail/string_float_tuple__struct.h"

/// Struct defined in msg/PoseList in the package custom_interfaces.
typedef struct custom_interfaces__msg__PoseList
{
  custom_interfaces__msg__StringFloatTuple__Sequence data;
} custom_interfaces__msg__PoseList;

// Struct for a sequence of custom_interfaces__msg__PoseList.
typedef struct custom_interfaces__msg__PoseList__Sequence
{
  custom_interfaces__msg__PoseList * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__msg__PoseList__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__POSE_LIST__STRUCT_H_
