# api_throttler


## Description

A simple limiter for outbound API requests.


## Installation

Uses only Python stdlib. Version is noted in toml.


## Usage

limit.py <--- contains the limiter code
class.py <--- shows one implementation, modeled after my current API setup.

\practice <--- contains example(s) of using my code for my own practice.


## Key Concepts

- Uses a decorator to add additional logic to a main class's request function.
  - Benefits:
      - Improved readability and reduced code.
      - Subclasses can inherit the logic without extra calling
   
- Handles the state of each API endpoint subclass. (I don't know how well)


## Future Improvements

- Timestamps are stored completely in RAM. Needs permanent storage to track states when program is restarted.
- My class structure most likely needs to be cleaned up someway.
- No testing.
