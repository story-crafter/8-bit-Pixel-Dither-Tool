# StoryCrafter Bayer 8×8 Ordered Dither Tool

A lightweight Bayer 8×8 ordered dithering implementation developed and used by **StoryCrafter** during game and visual asset production.

一个由 **StoryCrafter** 在游戏与美术开发过程中整理并使用的 Bayer 8×8 有序抖动工具。

[简体中文](#简体中文) · [English](#english)

---

## 简体中文

### 工具简介

这个工具可以在颜色量化或像素化处理前，为图像加入规律性的亮度偏移，从而减少明显的色阶断层，并形成更自然的像素颗粒与过渡层次。

### StoryCrafter 是什么？

[StoryCrafter](https://storycrafter.ai) 是一个 AI 互动叙事与文字冒险游戏创作平台。

我们希望帮助创作者更轻松地制作和发布互动故事、跑团模组与文字游戏，并通过 AI 游戏引擎，将剧本快速转化为可以直接游玩的体验。

### 为什么开源这个工具？

这个工具最初来自 StoryCrafter 自己的游戏与美术开发流程。

在制作像素风素材、角色图、场景图和网页视觉效果时，Bayer 8×8 有序抖动帮助我们：

* 减少有限色板下明显的色阶断层
* 保留像素画的颗粒感与层次
* 让同一组参数产生稳定、可复现的结果
* 快速将普通图像处理成更适合游戏使用的视觉素材

它在我们的实际开发中发挥了很大作用，因此我们决定将实现开源，希望也能帮助独立游戏开发者、像素艺术创作者和其他工具开发者。

### 支持与关注 StoryCrafter

如果这个工具对你有帮助，欢迎：

* ⭐ 给这个 GitHub 仓库点一个 Star
* 🎮 在 [Steam 上将 Story Crafter 加入愿望单](https://store.steampowered.com/app/3029600/Story_Crafter/)
* 🌐 访问 [StoryCrafter 官网](https://storycrafter.ai)
* 📺 关注我们的 [哔哩哔哩账号](https://space.bilibili.com/335309)
* 📕 关注我们的 [小红书账号](https://www.xiaohongshu.com/user/profile/62cd058c000000000e00c8f5)
* 𝕏 关注我们的 [X / Twitter 账号](https://x.com/StoryCrafter_AI)

你也可以把使用这个工具制作的作品分享给我们。我们很期待看到它被用于不同的游戏、美术项目和创作工具中。

### 工作原理

Bayer 8×8 有序抖动是一种确定性的图像抖动方法。

它通过固定的 8×8 阈值矩阵，为不同坐标的像素分配不同的亮暗偏移。矩阵会在整张图片上重复平铺，因此同一输入与同一参数始终会得到相同结果。

该方法通常用于缓解颜色量化后的色阶断层。在图像被映射到少量颜色之前，抖动会让相邻像素按照固定规律略微变亮或变暗。后续进行最近色量化时，相近亮度区域会被分配到不同的目标颜色，从而形成像素颗粒与过渡层次。

### 处理流程

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

### 使用与二次创作

欢迎在个人项目、商业项目、游戏、美术工具和其他开源项目中使用、修改与二次开发。

根据 Apache License 2.0，重新分发本项目或其衍生版本时，请保留：

* Apache License 2.0 协议文本
* 原始版权与署名信息
* 本仓库中的 `NOTICE` 文件内容
* 对修改过的文件作出明确说明

我们也非常感谢你在项目说明、README、鸣谢页面或相关发布内容中写明：

> Based on the StoryCrafter Bayer 8×8 Ordered Dither Tool
> https://github.com/story-crafter/8-bit-Pixel-Dither-Tool

这条推广性鸣谢是我们的友好请求，不会额外修改 Apache License 2.0 的法律条款。

---

## English

### About the Tool

This tool applies a deterministic Bayer 8×8 ordered dithering pattern before color quantization or pixel-art processing. It helps reduce visible color banding while creating more natural pixel texture and tonal transitions.

### What Is StoryCrafter?

[StoryCrafter](https://storycrafter.ai) is an AI-powered interactive storytelling and text-adventure creation platform.

We help creators build and publish interactive stories, tabletop role-playing modules, and text-based games, then turn their scripts into playable experiences through our AI game engine.

### Why Did We Open Source It?

This tool was originally created for StoryCrafter's own game and visual asset production workflow.

We use Bayer 8×8 ordered dithering to:

* Reduce visible banding when working with limited color palettes
* Preserve texture and depth in pixel-style artwork
* Produce stable and reproducible results with the same settings
* Quickly adapt regular images for use in games and interactive experiences

It has been genuinely useful in our development process, so we are releasing the implementation in the hope that it can also help indie developers, pixel artists, and tool creators.

### Support and Follow StoryCrafter

If this tool is useful to you, please consider:

* ⭐ Starring this GitHub repository
* 🎮 [Adding Story Crafter to your Steam wishlist](https://store.steampowered.com/app/3029600/Story_Crafter/)
* 🌐 Visiting the [StoryCrafter website](https://storycrafter.ai)
* 📺 Following us on [Bilibili](https://space.bilibili.com/335309)
* 📕 Following us on [Xiaohongshu](https://www.xiaohongshu.com/user/profile/62cd058c000000000e00c8f5)
* 𝕏 Following us on [X / Twitter](https://x.com/StoryCrafter_AI)

We would also love to see what you create with this tool. Feel free to share your games, artwork, or creative tools with us.

### How It Works

Bayer 8×8 ordered dithering is a deterministic image-dithering method.

A fixed 8×8 threshold matrix assigns a different brightness offset to each pixel position. The matrix repeats across the image, so the same input and settings always produce the same result.

Before an image is mapped to a limited set of colors, nearby pixels are made slightly brighter or darker according to this repeating pattern. During subsequent nearest-color quantization, similar areas may be assigned different target colors, producing pixel texture and smoother-looking tonal transitions.

### Processing Flow

```text
Input RGB image
  ↓
Read the Bayer 8×8 threshold for each pixel position
  ↓
Calculate the RGB brightness offset from the selected strength
  ↓
Apply the offset to the current pixel
  ↓
Output the dithered RGB image
```

### Usage and Derivative Works

You are welcome to use, modify, and build upon this project in personal projects, commercial projects, games, art tools, and other open-source software.

Under the Apache License 2.0, redistributed copies and derivative works must retain:

* A copy of the Apache License 2.0
* Applicable copyright and attribution notices
* The contents of this repository's `NOTICE` file
* Prominent notices identifying modified files

We would also appreciate the following credit in your project description, README, credits page, or related release materials:

> Based on the StoryCrafter Bayer 8×8 Ordered Dither Tool
> https://github.com/story-crafter/8-bit-Pixel-Dither-Tool

This promotional credit is a friendly request and does not add extra conditions to the Apache License 2.0.

---

## License

Copyright 2026 StoryCrafter Studio Inc.

Licensed under the [Apache License 2.0](LICENSE).

## StoryCrafter Links

* Website: https://storycrafter.ai
* Steam: https://store.steampowered.com/app/3029600/Story_Crafter/
* Bilibili: https://space.bilibili.com/335309
* Xiaohongshu: https://www.xiaohongshu.com/user/profile/62cd058c000000000e00c8f5
* X / Twitter: https://x.com/StoryCrafter_AI
* GitHub: https://github.com/story-crafter
