const BAYER_8X8 = [
  [0, 32, 8, 40, 2, 34, 10, 42],
  [48, 16, 56, 24, 50, 18, 58, 26],
  [12, 44, 4, 36, 14, 46, 6, 38],
  [60, 28, 52, 20, 62, 30, 54, 22],
  [3, 35, 11, 43, 1, 33, 9, 41],
  [51, 19, 59, 27, 49, 17, 57, 25],
  [15, 47, 7, 39, 13, 45, 5, 37],
  [63, 31, 55, 23, 61, 29, 53, 21],
];

/**
 * 对 Canvas ImageData 应用 Bayer 8×8 有序抖动。
 *
 * 注意：
 * - 这里只对 RGB 产生 Bayer 亮度偏移。
 * - alpha 通道保持不变。
 *
 * @param {ImageData} imageData Canvas 的 ImageData 对象
 * @param {number} strength 抖动强度，推荐范围 0~100
 * @returns {ImageData} 处理后的 ImageData
 */
function applyBayerOrderedDither(imageData, strength = 15) {
  if (!imageData || !imageData.data) {
    throw new TypeError('imageData 必须是有效的 ImageData 对象');
  }

  const data = imageData.data;
  const width = imageData.width;
  const height = imageData.height;

  const safeStrength = Math.max(0, Math.min(100, strength));
  const spread = (255 * safeStrength) / 100;

  const clamp = (value) => Math.max(0, Math.min(255, value));

  for (let y = 0; y < height; y += 1) {
    for (let x = 0; x < width; x += 1) {
      const bayerValue = BAYER_8X8[y % 8][x % 8];

      const threshold = (bayerValue + 0.5) / 64 - 0.5;

      const offset = threshold * spread;

      const pixelIndex = (y * width + x) * 4;

      data[pixelIndex] = clamp(data[pixelIndex] + offset);
      data[pixelIndex + 1] = clamp(data[pixelIndex + 1] + offset);
      data[pixelIndex + 2] = clamp(data[pixelIndex + 2] + offset);

    }
  }

  return imageData;
}
