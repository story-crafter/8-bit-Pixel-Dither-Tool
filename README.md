# StoryCrafter Bayer 8×8 Ordered Dither Tool

一个由 **StoryCrafter** 在游戏与美术开发过程中整理并使用的 Bayer 8×8 有序抖动工具。

它可以在颜色量化或像素化处理前，为图像加入规律性的亮度偏移，从而减少色阶断层，并形成更自然的像素颗粒与过渡层次。

## StoryCrafter 是什么？

[StoryCrafter](https://storycrafter.ai/zh) 是一个 AI 互动叙事与文字冒险游戏平台。

我们希望让创作者可以更轻松地制作和发布互动故事、跑团模组与文字游戏，并通过 AI 游戏引擎将剧本快速转化为可游玩的体验。

## 为什么开源这个工具？

这个工具最初来自 StoryCrafter 自己的游戏与美术开发流程。

在制作像素风素材、角色图、场景图和网页视觉效果时，Bayer 8×8 有序抖动帮助我们：

- 减少有限色板下明显的色阶断层
- 保留像素画的颗粒感与层次
- 让同一组参数产生稳定、可复现的结果
- 快速将普通图像处理成更适合游戏使用的视觉素材

它在我们的实际开发中发挥了很大作用，因此我们决定将实现开源，希望也能帮助独立游戏开发者、像素艺术创作者和其他工具开发者。

## 工作原理

Bayer 8×8 有序抖动是一种确定性的图像抖动方法。

它通过固定的 8×8 阈值矩阵，为不同坐标的像素分配不同的亮暗偏移。矩阵会在整张图片上重复平铺，因此同一输入与同一参数始终会得到相同结果。

该方法通常用于缓解颜色量化后的色阶断层。在图像被映射到少量颜色之前，抖动会让相邻像素按照固定规律略微变亮或变暗。后续进行最近色量化时，相近亮度区域会被分配到不同的目标颜色，从而形成像素颗粒与过渡层次。

## 处理流程

```text
输入 RGB 图像
  ↓
根据像素坐标读取 Bayer 8×8 阈值
  ↓
按照抖动强度计算 RGB 亮度偏移
  ↓
将偏移应用到当前像素
  ↓
输出抖动后的 RGB 图像
```

## 使用与二次创作

欢迎在个人项目、商业项目、游戏、美术工具和其他开源项目中使用、修改与二次开发。

根据 Apache License 2.0，重新分发本项目或其衍生版本时，请保留：

- Apache License 2.0 协议文本
- 原始版权与署名信息
- 本仓库中的 `NOTICE` 文件内容
- 对修改过的文件作出明确说明

我们也非常感谢你在项目说明、README、鸣谢页面或相关发布内容中写明：

> Based on the StoryCrafter Bayer 8×8 Ordered Dither Tool  
> https://github.com/story-crafter/8-bit-Pixel-Dither-Tool

这条推广性鸣谢是我们的友好请求，不会额外修改 Apache License 2.0 的法律条款。

## License

Copyright 2026 StoryCrafter Studio Inc.

Licensed under the [Apache License 2.0](LICENSE).

Apache License 2.0 允许个人与商业使用、修改和再分发，同时要求保留相应的许可证、版权及 NOTICE 署名信息。

## About StoryCrafter

- Website: https://storycrafter.ai
- GitHub: https://github.com/story-crafter
