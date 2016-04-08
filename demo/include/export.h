#ifndef LIB_COMMON_EXPORT_H_
#define LIB_COMMON_EXPORT_H_

#if defined(_WIN32)
#   if defined(LIB_COMMON_IMPLEMENTATION) || defined(LIB_APP_IMPLEMENTATION)
#       define APP_EXPORT __declspec(dllexport)
#   else
#       define APP_EXPORT __declspec(dllimport)
#   endif
#elif defined(__GNUC__)
#   if defined(LIB_COMMON_IMPLEMENTATION) || defined(LIB_APP_IMPLEMENTATION)
#       define APP_EXPORT __attribute__((visibility ("default")))
#   else
#       define APP_EXPORT
#   endif
#else
#   define ANGLE_EXPORT
#endif

#endif // LIB_COMMON_EXPORT_H_
