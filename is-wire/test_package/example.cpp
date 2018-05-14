#include "is/msgs/image.pb.h"
#include "is/wire/core.hpp"
#include "is/wire/rpc.hpp"
#include "is/wire/rpc/log-interceptor.hpp"
#include "is/wire/rpc/metrics-interceptor.hpp"

int main() {
  is::vision::Image image;
  is::Message msg{image};

  is::LogInterceptor logs;
  auto status = is::make_status(is::wire::StatusCode::OK);

  try {
    auto channel = is::Channel{"hodor"};
    auto provider = is::ServiceProvider{channel};
  } catch (...) {}
}
