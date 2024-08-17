"""
@author: wmpmiles
@title: GTF Utilities
@nickname: GTFU
@description: TODO
"""

import sys
from pathlib import Path
package_path = Path(__file__).resolve().parent
sys.path += [str(package_path)]
from gtf_nodes import interface, bbox, resample, dimensions, colorspace, \
    filter, math, transform, tonemap, convert  # noqa: E402
sys.path = sys.path[:-1]


NODE_CLASS_MAPPINGS = {
    # Interface
    "GTF | From Images":    interface.FromImages,
    "GTF | From Masks":     interface.FromMasks,
    "GTF | From Latents":   interface.FromLatents,
    "GTF | To Images":      interface.ToImages,
    "GTF | To Masks":       interface.ToMasks,
    "GTF | Update Latents": interface.UpdateLatents,
    # Resample
    "GTF | Resample - Nearest Neighbor":   resample.NearestNeighbor,
    "GTF | Resample - Area":               resample.Area,
    "GTF | Resample - Triangle":           resample.Triangle,
    "GTF | Resample - Mitchell-Netravali": resample.MitchellNetravali,
    "GTF | Resample - Lanczos":            resample.Lanczos,
    # Filter
    "GTF | Filter - Gaussian Blur": filter.BlurGaussian,
    "GTF | Filter - Morphological": filter.MorphologicalFilter,
    # Colorspace
    "GTF | Colorspace - SRGB Linear to Gamma": colorspace.SRGBLinearToGamma,
    "GTF | Colorspace - SRGB Gamma to Linear": colorspace.SRGBGammaToLinear,
    # Transform
    "GTF | Transform - Crop/Uncrop with Anchor": transform.CropUncropRelative,
    "GTF | Transform - Batch":                   transform.Batch,
    "GTF | Transform - Crop to BBOX":            transform.CropToBBOX,
    "GTF | Transform - Uncrop from BBOX":        transform.UncropFromBBOX,
    "GTF | Transform - Connected Components":    transform.ConnectedComponents,
    "GTF | Transform - 1 Channel to 3":          transform.Channels1To3Repeat,
    "GTF | Transform - 1 Channel to 4":          transform.Channels1To4Repeat,
    # Arithmetic
    "GTF | Math - Zero":       math.Zero,
    "GTF | Math - One":        math.One,
    "GTF | Math - Float":      math.Float,
    "GTF | Math - Add":        math.Add,
    "GTF | Math - Multiply":   math.Multiply,
    "GTF | Math - Reciprocal": math.Reciprocal,
    "GTF | Math - Negative":   math.Negate,
    "GTF | Math - Lerp":       math.Lerp,
    "GTF | Math - Pow":        math.Pow,
    # Tonemap
    "GTF | Tonemap - Reinhard":                tonemap.Reinhard,
    "GTF | Tonemap - Reinhard Extended":       tonemap.ReinhardExtended,
    "GTF | Tonemap - Reinhard over Luminance": tonemap.ReinhardLuminance,
    "GTF | Tonemap - Reinhard Extended over Luminance":
    tonemap.ReinhardExtendedLuminance,
    "GTF | Tonemap - Reinhard-Jodie":          tonemap.ReinhardJodie,
    "GTF | Tonemap - Reinhard-Jodie Extended": tonemap.ReinhardJodieExtended,
    "GTF | Tonemap - Uncharted 2":             tonemap.Uncharted2,
    "GTF | Tonemap - ACES":                    tonemap.ACES,
    # Convert
    "GTF | Convert - Luminance":   convert.Luminance,
    "GTF | Convert - Min":         convert.Min,
    "GTF | Convert - Max":         convert.Max,
    "GTF | Convert - Batch Min":   convert.BatchMin,
    "GTF | Convert - Batch Max":   convert.BatchMax,
    "GTF | Convert - Channel Min": convert.ChannelMin,
    "GTF | Convert - Channel Max": convert.ChannelMax,
    # BBOX
    "BBOX | From Mask":  bbox.FromMask,
    "BBOX | Change":     bbox.Change,
    "BBOX | Scale Area": bbox.AreaScale,
    # Dimensions
    "Dimensions | Scale":               dimensions.Scale,
    "Dimensions | Change":              dimensions.Change,
    "Dimensions | Scale to Megapixels": dimensions.ScaleToMegapixels,
    "Dimensions | Align To":            dimensions.AlignTo,
    "Dimensions | From Raw":            dimensions.FromRaw,
    "Dimensions | To Raw":              dimensions.ToRaw,
    "Dimensions | From GTF":            dimensions.FromGTF,
}


__all__ = ["NODE_CLASS_MAPPINGS"]
