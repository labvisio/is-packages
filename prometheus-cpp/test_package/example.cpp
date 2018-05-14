#include "prometheus/exposer.h"
#include "prometheus/registry.h"

int main() {
  auto registry = std::make_shared<prometheus::Registry>();
}
