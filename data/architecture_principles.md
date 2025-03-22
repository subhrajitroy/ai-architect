# Architecture Principles

## Build for scale

- Systems should be able to scale horizontally to handle increased load.
- Avoid sticky components that cannot be scaled horizontally.
- Reduce database load by using caching.
- Build services with the right boundaries to avoid unnecessary dependencies.



**Example:** Avoid sticky sessions by using a load balancer to distribute requests evenly across multiple instances of a service.Slow changing data like reference data can be cached to reduce database load.

## Design for Resilience

- Where possible, design services to be stateless and idempotent.
- Implement circuit breakers to prevent cascading failures.
- Implement retry logic with exponential backoff.
- Implement timeouts to prevent slow requests from blocking other requests.
- Use messaging to decouple services and improve resilience.



**Example:** Identify the minimum amount of work that needs to be done synchronously and implement a queue to handle the rest.

## Recommended Tech Stack

- Database: PostgreSQL should be used as the primary relational database for persistent data storage.
- Cache: Redis should be implemented for caching and temporary data storage to improve performance.
- Programming Language: Java is the standard language for backend development.
- Framework: Spring Boot is the approved framework for building Java applications.

**Example:** When developing a new microservice, it should be built using Java with Spring Boot, store its data in PostgreSQL, and use Redis for caching frequently accessed data or managing session state. 