// macOS Vision subject lift: swift cutout.swift in.png out.png  (free, on-device)
import Vision
import CoreImage
import AppKit
let a = CommandLine.arguments
let ci = CIImage(contentsOf: URL(fileURLWithPath: a[1]))!
let req = VNGenerateForegroundInstanceMaskRequest()
let h = VNImageRequestHandler(ciImage: ci)
try h.perform([req])
let r = req.results!.first!
let mask = try r.generateScaledMaskForImage(forInstances: r.allInstances, from: h)
let out = ci.applyingFilter("CIBlendWithMask", parameters: [kCIInputBackgroundImageKey: CIImage.empty(), kCIInputMaskImageKey: CIImage(cvPixelBuffer: mask)])
let ctx = CIContext()
try ctx.writePNGRepresentation(of: out, to: URL(fileURLWithPath: a[2]), format: CIFormat.RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!)
