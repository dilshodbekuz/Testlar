import Foundation
import Vision
import CoreGraphics
import ImageIO

let args = CommandLine.arguments
guard args.count > 1 else { print("usage: ocr <pdf> [firstPage] [lastPage]"); exit(1) }
let url = URL(fileURLWithPath: args[1])
let p1 = args.count > 2 ? Int(args[2])! : 1
let p2 = args.count > 3 ? Int(args[3])! : p1
guard let doc = CGPDFDocument(url as CFURL) else { print("pdf ochilmadi"); exit(1) }

for i in p1...min(p2, doc.numberOfPages) {
    guard let page = doc.page(at: i) else { continue }
    let box = page.getBoxRect(.mediaBox)
    let scale: CGFloat = 3.0
    let w = Int(box.width * scale), h = Int(box.height * scale)
    let cs = CGColorSpaceCreateDeviceGray()
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8,
                             bytesPerRow: 0, space: cs,
                             bitmapInfo: CGImageAlphaInfo.none.rawValue) else { continue }
    ctx.setFillColor(gray: 1, alpha: 1)
    ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.scaleBy(x: scale, y: scale)
    ctx.drawPDFPage(page)
    guard let img = ctx.makeImage() else { continue }

    let req = VNRecognizeTextRequest()
    req.recognitionLevel = .accurate
    req.usesLanguageCorrection = true
    req.recognitionLanguages = ["en-US"]
    let handler = VNImageRequestHandler(cgImage: img, options: [:])
    try? handler.perform([req])
    print("=== SAHIFA \(i) ===")
    for obs in (req.results ?? []) {
        if let c = obs.topCandidates(1).first { print(c.string) }
    }
}
