class Solver
  def call(people)
    # 1. Get min and max year
    min_year, max_year = get_min_max_year(people)

    # 2. Create lookup hash
    lookup = Hash.new(0)

    # 3. Assign the differences
    people.each do |born, death|
      lookup[born  - min_year    ] += 1
      lookup[death - min_year + 1] -= 1
    end

    # 4. Find max accumulated sum of people
    acc = 0
    max_people = 0
    max_index = -1

    (0..(max_year - min_year + 1)).each do |index|
      acc += lookup[index]

      if acc > max_people
        max_people = acc
        max_index  = index
      end
    end

    min_year + max_index
  end

  private

  def get_min_max_year(people)
    min, max = nil, nil

    people.each do |born, death|
      min = born  if min.nil? || min > born
      max = death if max.nil? || max < death
    end

    [min, max]
  end
end
