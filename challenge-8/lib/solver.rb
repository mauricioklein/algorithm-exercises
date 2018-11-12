class Solver
  def call(str)
    lookup = Hash.new(0)
    num_count = 0

    # 1. Populate lookup & num_count
    str.split(//).each do |ch|
      if number?(ch)
        num_count += ch.to_i
      else
        lookup[ch] += 1
      end
    end

    buffer = ""

    # 2. Insert chars in the buffer
    ('A'..'Z').each do |ch|
      buffer += ch * lookup[ch]
    end

    # 3. Insert sum of digits to the end of buffer
    buffer += num_count.to_s

    return buffer
  end

  private

  def number?(ch)
    ch =~ /[0-9]/
  end
end
