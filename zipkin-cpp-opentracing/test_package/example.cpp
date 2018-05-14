#include "zipkin/opentracing.h"

int main() {
  using namespace zipkin;
  using namespace opentracing;

  ZipkinOtTracerOptions options;
  options.service_name = "Tutorial";
  auto tracer = makeZipkinOtTracer(options);

  auto parent_span = tracer->StartSpan("parent");
}
