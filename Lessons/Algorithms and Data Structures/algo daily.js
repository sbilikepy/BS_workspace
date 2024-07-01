/**
 * @param {number} x
 *
 * @returns {number}
 */
function sqrt(x) {
  if (x < 2) {
    return x;
  }

  let left = 2;
  let right = Math.floor(x / 2);

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    const num = mid * mid;

    if (num === x) {
      return mid;
    } else if (num < x) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return right;
}


/**
 * @param {number[]} arr
 *
 * @returns {number}
 */
function peakIndexInMountainArray(arr) {
  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    const mid = Math.floor((left + right) / 2);

    if (arr[mid] < arr[mid + 1]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }

  return left;
}
