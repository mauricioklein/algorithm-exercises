class Solver
  def call(steps)
    steps_lookup = {}

    calculate_steps(steps, steps_lookup)
  end

  private

  def calculate_steps(remaining_steps, steps_lookup)
    return 1 if remaining_steps < 2

    steps_lookup[remaining_steps - 1] ||= calculate_steps(remaining_steps - 1, steps_lookup)
    steps_lookup[remaining_steps - 2] ||= calculate_steps(remaining_steps - 2, steps_lookup)

    steps_lookup[remaining_steps - 1] + steps_lookup[remaining_steps - 2]
  end
end
