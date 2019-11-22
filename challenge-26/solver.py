def courses_to_take(input):
  """
  Time complexity: O(n) (we process each course only once)
  Space complexity: O(n) (array to store the result)
  """
  # Normalize the dependencies, using a set to track the
  # dependencies more efficiently
  course_with_deps = {}
  to_take = []

  for course, deps in input.items():
    if not deps:
      # Course with no dependencies:
      # candidate to start the search
      to_take.append(course)
    else:
      course_with_deps[course] = set(deps)

  result = []
  while to_take:
    course = to_take.pop()

    # Add course to journey
    result.append(course)

    # Iterate through courses and remove this course from
    # dependencies
    for prereq_course, prereq_deps in course_with_deps.items():
      if course in prereq_deps:
        prereq_deps.remove(course)
      
      if not prereq_deps:
        # Course has all the dependencies solved:
        # add to the "to_take" queue
        to_take.append(prereq_course)
        del course_with_deps[prereq_course]

  return result if len(result) == len(input) else None
