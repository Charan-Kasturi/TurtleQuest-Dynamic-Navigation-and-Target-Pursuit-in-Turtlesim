// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from custom_interfaces:msg/NewTurtlePose.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__MSG__DETAIL__NEW_TURTLE_POSE__STRUCT_H_
#define CUSTOM_INTERFACES__MSG__DETAIL__NEW_TURTLE_POSE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/NewTurtlePose in the package custom_interfaces.
typedef struct custom_interfaces__msg__NewTurtlePose
{
  rosidl_runtime_c__String name;
  float x;
  float y;
  float theta;
} custom_interfaces__msg__NewTurtlePose;

// Struct for a sequence of custom_interfaces__msg__NewTurtlePose.
typedef struct custom_interfaces__msg__NewTurtlePose__Sequence
{
  custom_interfaces__msg__NewTurtlePose * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} custom_interfaces__msg__NewTurtlePose__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // CUSTOM_INTERFACES__MSG__DETAIL__NEW_TURTLE_POSE__STRUCT_H_
