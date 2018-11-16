class Solver
  def call(arr, k)
    k_index = k - 1

    quick_select(arr, k_index, 0, arr.length - 1)

    arr[0..k_index]
  end

  private

  def quick_select(arr, k, left, right)
    # Single element = already sorted
    return if left >= right

    wall, pivot = left, right

    for current in (left..(right - 1))
      if arr[current] <= arr[pivot]
        swap(arr, current, wall)
        wall += 1
      end
    end

    # Put pivot on the right position
    swap(arr, wall, pivot)
    pivot = wall

    # K index found
    return if pivot == k

    if k < pivot
      quick_select(arr, k, left, pivot - 1)
    else
      quick_select(arr, k, pivot + 1, right)
    end
  end

  def swap(arr, i, j)
    arr[i], arr[j] = arr[j], arr[i]
  end
end
