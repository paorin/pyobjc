# This file is generated by objective.metadata
#
# Last update: Sun Jul 11 23:13:28 2021
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a


else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$kCFErrorDomainCGImageMetadata$kCGImageAnimationDelayTime$kCGImageAnimationLoopCount$kCGImageAnimationStartIndex$kCGImageAuxiliaryDataInfoData$kCGImageAuxiliaryDataInfoDataDescription$kCGImageAuxiliaryDataInfoMetadata$kCGImageAuxiliaryDataTypeDepth$kCGImageAuxiliaryDataTypeDisparity$kCGImageAuxiliaryDataTypeHDRGainMap$kCGImageAuxiliaryDataTypePortraitEffectsMatte$kCGImageAuxiliaryDataTypeSemanticSegmentationGlassesMatte$kCGImageAuxiliaryDataTypeSemanticSegmentationHairMatte$kCGImageAuxiliaryDataTypeSemanticSegmentationSkinMatte$kCGImageAuxiliaryDataTypeSemanticSegmentationSkyMatte$kCGImageAuxiliaryDataTypeSemanticSegmentationTeethMatte$kCGImageDestinationBackgroundColor$kCGImageDestinationDateTime$kCGImageDestinationEmbedThumbnail$kCGImageDestinationImageMaxPixelSize$kCGImageDestinationLossyCompressionQuality$kCGImageDestinationMergeMetadata$kCGImageDestinationMetadata$kCGImageDestinationOptimizeColorForSharing$kCGImageDestinationOrientation$kCGImageDestinationPreserveGainMap$kCGImageMetadataEnumerateRecursively$kCGImageMetadataNamespaceDublinCore$kCGImageMetadataNamespaceExif$kCGImageMetadataNamespaceExifAux$kCGImageMetadataNamespaceExifEX$kCGImageMetadataNamespaceIPTCCore$kCGImageMetadataNamespaceIPTCExtension$kCGImageMetadataNamespacePhotoshop$kCGImageMetadataNamespaceTIFF$kCGImageMetadataNamespaceXMPBasic$kCGImageMetadataNamespaceXMPRights$kCGImageMetadataPrefixDublinCore$kCGImageMetadataPrefixExif$kCGImageMetadataPrefixExifAux$kCGImageMetadataPrefixExifEX$kCGImageMetadataPrefixIPTCCore$kCGImageMetadataPrefixIPTCExtension$kCGImageMetadataPrefixPhotoshop$kCGImageMetadataPrefixTIFF$kCGImageMetadataPrefixXMPBasic$kCGImageMetadataPrefixXMPRights$kCGImageMetadataShouldExcludeGPS$kCGImageMetadataShouldExcludeXMP$kCGImageProperty8BIMDictionary$kCGImageProperty8BIMLayerNames$kCGImageProperty8BIMVersion$kCGImagePropertyAPNGCanvasPixelHeight$kCGImagePropertyAPNGCanvasPixelWidth$kCGImagePropertyAPNGDelayTime$kCGImagePropertyAPNGFrameInfoArray$kCGImagePropertyAPNGLoopCount$kCGImagePropertyAPNGUnclampedDelayTime$kCGImagePropertyAuxiliaryData$kCGImagePropertyAuxiliaryDataType$kCGImagePropertyBytesPerRow$kCGImagePropertyCIFFCameraSerialNumber$kCGImagePropertyCIFFContinuousDrive$kCGImagePropertyCIFFDescription$kCGImagePropertyCIFFDictionary$kCGImagePropertyCIFFFirmware$kCGImagePropertyCIFFFlashExposureComp$kCGImagePropertyCIFFFocusMode$kCGImagePropertyCIFFImageFileName$kCGImagePropertyCIFFImageName$kCGImagePropertyCIFFImageSerialNumber$kCGImagePropertyCIFFLensMaxMM$kCGImagePropertyCIFFLensMinMM$kCGImagePropertyCIFFLensModel$kCGImagePropertyCIFFMeasuredEV$kCGImagePropertyCIFFMeteringMode$kCGImagePropertyCIFFOwnerName$kCGImagePropertyCIFFRecordID$kCGImagePropertyCIFFReleaseMethod$kCGImagePropertyCIFFReleaseTiming$kCGImagePropertyCIFFSelfTimingTime$kCGImagePropertyCIFFShootingMode$kCGImagePropertyCIFFWhiteBalanceIndex$kCGImagePropertyColorModel$kCGImagePropertyColorModelCMYK$kCGImagePropertyColorModelGray$kCGImagePropertyColorModelLab$kCGImagePropertyColorModelRGB$kCGImagePropertyDNGActiveArea$kCGImagePropertyDNGAnalogBalance$kCGImagePropertyDNGAntiAliasStrength$kCGImagePropertyDNGAsShotICCProfile$kCGImagePropertyDNGAsShotNeutral$kCGImagePropertyDNGAsShotPreProfileMatrix$kCGImagePropertyDNGAsShotProfileName$kCGImagePropertyDNGAsShotWhiteXY$kCGImagePropertyDNGBackwardVersion$kCGImagePropertyDNGBaselineExposure$kCGImagePropertyDNGBaselineExposureOffset$kCGImagePropertyDNGBaselineNoise$kCGImagePropertyDNGBaselineSharpness$kCGImagePropertyDNGBayerGreenSplit$kCGImagePropertyDNGBestQualityScale$kCGImagePropertyDNGBlackLevel$kCGImagePropertyDNGBlackLevelDeltaH$kCGImagePropertyDNGBlackLevelDeltaV$kCGImagePropertyDNGBlackLevelRepeatDim$kCGImagePropertyDNGCFALayout$kCGImagePropertyDNGCFAPlaneColor$kCGImagePropertyDNGCalibrationIlluminant1$kCGImagePropertyDNGCalibrationIlluminant2$kCGImagePropertyDNGCameraCalibration1$kCGImagePropertyDNGCameraCalibration2$kCGImagePropertyDNGCameraCalibrationSignature$kCGImagePropertyDNGCameraSerialNumber$kCGImagePropertyDNGChromaBlurRadius$kCGImagePropertyDNGColorMatrix1$kCGImagePropertyDNGColorMatrix2$kCGImagePropertyDNGColorimetricReference$kCGImagePropertyDNGCurrentICCProfile$kCGImagePropertyDNGCurrentPreProfileMatrix$kCGImagePropertyDNGDefaultBlackRender$kCGImagePropertyDNGDefaultCropOrigin$kCGImagePropertyDNGDefaultCropSize$kCGImagePropertyDNGDefaultScale$kCGImagePropertyDNGDefaultUserCrop$kCGImagePropertyDNGDictionary$kCGImagePropertyDNGExtraCameraProfiles$kCGImagePropertyDNGFixVignetteRadial$kCGImagePropertyDNGForwardMatrix1$kCGImagePropertyDNGForwardMatrix2$kCGImagePropertyDNGLensInfo$kCGImagePropertyDNGLinearResponseLimit$kCGImagePropertyDNGLinearizationTable$kCGImagePropertyDNGLocalizedCameraModel$kCGImagePropertyDNGMakerNoteSafety$kCGImagePropertyDNGMaskedAreas$kCGImagePropertyDNGNewRawImageDigest$kCGImagePropertyDNGNoiseProfile$kCGImagePropertyDNGNoiseReductionApplied$kCGImagePropertyDNGOpcodeList1$kCGImagePropertyDNGOpcodeList2$kCGImagePropertyDNGOpcodeList3$kCGImagePropertyDNGOriginalBestQualityFinalSize$kCGImagePropertyDNGOriginalDefaultCropSize$kCGImagePropertyDNGOriginalDefaultFinalSize$kCGImagePropertyDNGOriginalRawFileData$kCGImagePropertyDNGOriginalRawFileDigest$kCGImagePropertyDNGOriginalRawFileName$kCGImagePropertyDNGPreviewApplicationName$kCGImagePropertyDNGPreviewApplicationVersion$kCGImagePropertyDNGPreviewColorSpace$kCGImagePropertyDNGPreviewDateTime$kCGImagePropertyDNGPreviewSettingsDigest$kCGImagePropertyDNGPreviewSettingsName$kCGImagePropertyDNGPrivateData$kCGImagePropertyDNGProfileCalibrationSignature$kCGImagePropertyDNGProfileCopyright$kCGImagePropertyDNGProfileEmbedPolicy$kCGImagePropertyDNGProfileHueSatMapData1$kCGImagePropertyDNGProfileHueSatMapData2$kCGImagePropertyDNGProfileHueSatMapDims$kCGImagePropertyDNGProfileHueSatMapEncoding$kCGImagePropertyDNGProfileLookTableData$kCGImagePropertyDNGProfileLookTableDims$kCGImagePropertyDNGProfileLookTableEncoding$kCGImagePropertyDNGProfileName$kCGImagePropertyDNGProfileToneCurve$kCGImagePropertyDNGRawDataUniqueID$kCGImagePropertyDNGRawImageDigest$kCGImagePropertyDNGRawToPreviewGain$kCGImagePropertyDNGReductionMatrix1$kCGImagePropertyDNGReductionMatrix2$kCGImagePropertyDNGRowInterleaveFactor$kCGImagePropertyDNGShadowScale$kCGImagePropertyDNGSubTileBlockSize$kCGImagePropertyDNGUniqueCameraModel$kCGImagePropertyDNGVersion$kCGImagePropertyDNGWarpFisheye$kCGImagePropertyDNGWarpRectilinear$kCGImagePropertyDNGWhiteLevel$kCGImagePropertyDPIHeight$kCGImagePropertyDPIWidth$kCGImagePropertyDepth$kCGImagePropertyExifApertureValue$kCGImagePropertyExifAuxDictionary$kCGImagePropertyExifAuxFirmware$kCGImagePropertyExifAuxFlashCompensation$kCGImagePropertyExifAuxImageNumber$kCGImagePropertyExifAuxLensID$kCGImagePropertyExifAuxLensInfo$kCGImagePropertyExifAuxLensModel$kCGImagePropertyExifAuxLensSerialNumber$kCGImagePropertyExifAuxOwnerName$kCGImagePropertyExifAuxSerialNumber$kCGImagePropertyExifBodySerialNumber$kCGImagePropertyExifBrightnessValue$kCGImagePropertyExifCFAPattern$kCGImagePropertyExifCameraOwnerName$kCGImagePropertyExifColorSpace$kCGImagePropertyExifComponentsConfiguration$kCGImagePropertyExifCompositeImage$kCGImagePropertyExifCompressedBitsPerPixel$kCGImagePropertyExifContrast$kCGImagePropertyExifCustomRendered$kCGImagePropertyExifDateTimeDigitized$kCGImagePropertyExifDateTimeOriginal$kCGImagePropertyExifDeviceSettingDescription$kCGImagePropertyExifDictionary$kCGImagePropertyExifDigitalZoomRatio$kCGImagePropertyExifExposureBiasValue$kCGImagePropertyExifExposureIndex$kCGImagePropertyExifExposureMode$kCGImagePropertyExifExposureProgram$kCGImagePropertyExifExposureTime$kCGImagePropertyExifFNumber$kCGImagePropertyExifFileSource$kCGImagePropertyExifFlash$kCGImagePropertyExifFlashEnergy$kCGImagePropertyExifFlashPixVersion$kCGImagePropertyExifFocalLenIn35mmFilm$kCGImagePropertyExifFocalLength$kCGImagePropertyExifFocalPlaneResolutionUnit$kCGImagePropertyExifFocalPlaneXResolution$kCGImagePropertyExifFocalPlaneYResolution$kCGImagePropertyExifGainControl$kCGImagePropertyExifGamma$kCGImagePropertyExifISOSpeed$kCGImagePropertyExifISOSpeedLatitudeyyy$kCGImagePropertyExifISOSpeedLatitudezzz$kCGImagePropertyExifISOSpeedRatings$kCGImagePropertyExifImageUniqueID$kCGImagePropertyExifLensMake$kCGImagePropertyExifLensModel$kCGImagePropertyExifLensSerialNumber$kCGImagePropertyExifLensSpecification$kCGImagePropertyExifLightSource$kCGImagePropertyExifMakerNote$kCGImagePropertyExifMaxApertureValue$kCGImagePropertyExifMeteringMode$kCGImagePropertyExifOECF$kCGImagePropertyExifOffsetTime$kCGImagePropertyExifOffsetTimeDigitized$kCGImagePropertyExifOffsetTimeOriginal$kCGImagePropertyExifPixelXDimension$kCGImagePropertyExifPixelYDimension$kCGImagePropertyExifRecommendedExposureIndex$kCGImagePropertyExifRelatedSoundFile$kCGImagePropertyExifSaturation$kCGImagePropertyExifSceneCaptureType$kCGImagePropertyExifSceneType$kCGImagePropertyExifSensingMethod$kCGImagePropertyExifSensitivityType$kCGImagePropertyExifSharpness$kCGImagePropertyExifShutterSpeedValue$kCGImagePropertyExifSourceExposureTimesOfCompositeImage$kCGImagePropertyExifSourceImageNumberOfCompositeImage$kCGImagePropertyExifSpatialFrequencyResponse$kCGImagePropertyExifSpectralSensitivity$kCGImagePropertyExifStandardOutputSensitivity$kCGImagePropertyExifSubjectArea$kCGImagePropertyExifSubjectDistRange$kCGImagePropertyExifSubjectDistance$kCGImagePropertyExifSubjectLocation$kCGImagePropertyExifSubsecTime$kCGImagePropertyExifSubsecTimeDigitized$kCGImagePropertyExifSubsecTimeOrginal$kCGImagePropertyExifSubsecTimeOriginal$kCGImagePropertyExifUserComment$kCGImagePropertyExifVersion$kCGImagePropertyExifWhiteBalance$kCGImagePropertyFileContentsDictionary$kCGImagePropertyFileSize$kCGImagePropertyGIFCanvasPixelHeight$kCGImagePropertyGIFCanvasPixelWidth$kCGImagePropertyGIFDelayTime$kCGImagePropertyGIFDictionary$kCGImagePropertyGIFFrameInfoArray$kCGImagePropertyGIFHasGlobalColorMap$kCGImagePropertyGIFImageColorMap$kCGImagePropertyGIFLoopCount$kCGImagePropertyGIFUnclampedDelayTime$kCGImagePropertyGPSAltitude$kCGImagePropertyGPSAltitudeRef$kCGImagePropertyGPSAreaInformation$kCGImagePropertyGPSDOP$kCGImagePropertyGPSDateStamp$kCGImagePropertyGPSDestBearing$kCGImagePropertyGPSDestBearingRef$kCGImagePropertyGPSDestDistance$kCGImagePropertyGPSDestDistanceRef$kCGImagePropertyGPSDestLatitude$kCGImagePropertyGPSDestLatitudeRef$kCGImagePropertyGPSDestLongitude$kCGImagePropertyGPSDestLongitudeRef$kCGImagePropertyGPSDictionary$kCGImagePropertyGPSDifferental$kCGImagePropertyGPSHPositioningError$kCGImagePropertyGPSImgDirection$kCGImagePropertyGPSImgDirectionRef$kCGImagePropertyGPSLatitude$kCGImagePropertyGPSLatitudeRef$kCGImagePropertyGPSLongitude$kCGImagePropertyGPSLongitudeRef$kCGImagePropertyGPSMapDatum$kCGImagePropertyGPSMeasureMode$kCGImagePropertyGPSProcessingMethod$kCGImagePropertyGPSSatellites$kCGImagePropertyGPSSpeed$kCGImagePropertyGPSSpeedRef$kCGImagePropertyGPSStatus$kCGImagePropertyGPSTimeStamp$kCGImagePropertyGPSTrack$kCGImagePropertyGPSTrackRef$kCGImagePropertyGPSVersion$kCGImagePropertyGroupImageIndexLeft$kCGImagePropertyGroupImageIndexRight$kCGImagePropertyGroupImageIsAlternateImage$kCGImagePropertyGroupImageIsLeftImage$kCGImagePropertyGroupImageIsRightImage$kCGImagePropertyGroupImagesAlternate$kCGImagePropertyGroupIndex$kCGImagePropertyGroupType$kCGImagePropertyGroupTypeAlternate$kCGImagePropertyGroupTypeStereoPair$kCGImagePropertyGroups$kCGImagePropertyHEICSCanvasPixelHeight$kCGImagePropertyHEICSCanvasPixelWidth$kCGImagePropertyHEICSDelayTime$kCGImagePropertyHEICSDictionary$kCGImagePropertyHEICSFrameInfoArray$kCGImagePropertyHEICSLoopCount$kCGImagePropertyHEICSUnclampedDelayTime$kCGImagePropertyHasAlpha$kCGImagePropertyHeight$kCGImagePropertyIPTCActionAdvised$kCGImagePropertyIPTCByline$kCGImagePropertyIPTCBylineTitle$kCGImagePropertyIPTCCaptionAbstract$kCGImagePropertyIPTCCategory$kCGImagePropertyIPTCCity$kCGImagePropertyIPTCContact$kCGImagePropertyIPTCContactInfoAddress$kCGImagePropertyIPTCContactInfoCity$kCGImagePropertyIPTCContactInfoCountry$kCGImagePropertyIPTCContactInfoEmails$kCGImagePropertyIPTCContactInfoPhones$kCGImagePropertyIPTCContactInfoPostalCode$kCGImagePropertyIPTCContactInfoStateProvince$kCGImagePropertyIPTCContactInfoWebURLs$kCGImagePropertyIPTCContentLocationCode$kCGImagePropertyIPTCContentLocationName$kCGImagePropertyIPTCCopyrightNotice$kCGImagePropertyIPTCCountryPrimaryLocationCode$kCGImagePropertyIPTCCountryPrimaryLocationName$kCGImagePropertyIPTCCreatorContactInfo$kCGImagePropertyIPTCCredit$kCGImagePropertyIPTCDateCreated$kCGImagePropertyIPTCDictionary$kCGImagePropertyIPTCDigitalCreationDate$kCGImagePropertyIPTCDigitalCreationTime$kCGImagePropertyIPTCEditStatus$kCGImagePropertyIPTCEditorialUpdate$kCGImagePropertyIPTCExpirationDate$kCGImagePropertyIPTCExpirationTime$kCGImagePropertyIPTCExtAboutCvTerm$kCGImagePropertyIPTCExtAboutCvTermCvId$kCGImagePropertyIPTCExtAboutCvTermId$kCGImagePropertyIPTCExtAboutCvTermName$kCGImagePropertyIPTCExtAboutCvTermRefinedAbout$kCGImagePropertyIPTCExtAddlModelInfo$kCGImagePropertyIPTCExtArtworkCircaDateCreated$kCGImagePropertyIPTCExtArtworkContentDescription$kCGImagePropertyIPTCExtArtworkContributionDescription$kCGImagePropertyIPTCExtArtworkCopyrightNotice$kCGImagePropertyIPTCExtArtworkCopyrightOwnerID$kCGImagePropertyIPTCExtArtworkCopyrightOwnerName$kCGImagePropertyIPTCExtArtworkCreator$kCGImagePropertyIPTCExtArtworkCreatorID$kCGImagePropertyIPTCExtArtworkDateCreated$kCGImagePropertyIPTCExtArtworkLicensorID$kCGImagePropertyIPTCExtArtworkLicensorName$kCGImagePropertyIPTCExtArtworkOrObject$kCGImagePropertyIPTCExtArtworkPhysicalDescription$kCGImagePropertyIPTCExtArtworkSource$kCGImagePropertyIPTCExtArtworkSourceInvURL$kCGImagePropertyIPTCExtArtworkSourceInventoryNo$kCGImagePropertyIPTCExtArtworkStylePeriod$kCGImagePropertyIPTCExtArtworkTitle$kCGImagePropertyIPTCExtAudioBitrate$kCGImagePropertyIPTCExtAudioBitrateMode$kCGImagePropertyIPTCExtAudioChannelCount$kCGImagePropertyIPTCExtCircaDateCreated$kCGImagePropertyIPTCExtContainerFormat$kCGImagePropertyIPTCExtContainerFormatIdentifier$kCGImagePropertyIPTCExtContainerFormatName$kCGImagePropertyIPTCExtContributor$kCGImagePropertyIPTCExtContributorIdentifier$kCGImagePropertyIPTCExtContributorName$kCGImagePropertyIPTCExtContributorRole$kCGImagePropertyIPTCExtControlledVocabularyTerm$kCGImagePropertyIPTCExtCopyrightYear$kCGImagePropertyIPTCExtCreator$kCGImagePropertyIPTCExtCreatorIdentifier$kCGImagePropertyIPTCExtCreatorName$kCGImagePropertyIPTCExtCreatorRole$kCGImagePropertyIPTCExtDataOnScreen$kCGImagePropertyIPTCExtDataOnScreenRegion$kCGImagePropertyIPTCExtDataOnScreenRegionD$kCGImagePropertyIPTCExtDataOnScreenRegionH$kCGImagePropertyIPTCExtDataOnScreenRegionText$kCGImagePropertyIPTCExtDataOnScreenRegionUnit$kCGImagePropertyIPTCExtDataOnScreenRegionW$kCGImagePropertyIPTCExtDataOnScreenRegionX$kCGImagePropertyIPTCExtDataOnScreenRegionY$kCGImagePropertyIPTCExtDigitalImageGUID$kCGImagePropertyIPTCExtDigitalSourceFileType$kCGImagePropertyIPTCExtDigitalSourceType$kCGImagePropertyIPTCExtDopesheet$kCGImagePropertyIPTCExtDopesheetLink$kCGImagePropertyIPTCExtDopesheetLinkLink$kCGImagePropertyIPTCExtDopesheetLinkLinkQualifier$kCGImagePropertyIPTCExtEmbdEncRightsExpr$kCGImagePropertyIPTCExtEmbeddedEncodedRightsExpr$kCGImagePropertyIPTCExtEmbeddedEncodedRightsExprLangID$kCGImagePropertyIPTCExtEmbeddedEncodedRightsExprType$kCGImagePropertyIPTCExtEpisode$kCGImagePropertyIPTCExtEpisodeIdentifier$kCGImagePropertyIPTCExtEpisodeName$kCGImagePropertyIPTCExtEpisodeNumber$kCGImagePropertyIPTCExtEvent$kCGImagePropertyIPTCExtExternalMetadataLink$kCGImagePropertyIPTCExtFeedIdentifier$kCGImagePropertyIPTCExtGenre$kCGImagePropertyIPTCExtGenreCvId$kCGImagePropertyIPTCExtGenreCvTermId$kCGImagePropertyIPTCExtGenreCvTermName$kCGImagePropertyIPTCExtGenreCvTermRefinedAbout$kCGImagePropertyIPTCExtHeadline$kCGImagePropertyIPTCExtIPTCLastEdited$kCGImagePropertyIPTCExtLinkedEncRightsExpr$kCGImagePropertyIPTCExtLinkedEncodedRightsExpr$kCGImagePropertyIPTCExtLinkedEncodedRightsExprLangID$kCGImagePropertyIPTCExtLinkedEncodedRightsExprType$kCGImagePropertyIPTCExtLocationCity$kCGImagePropertyIPTCExtLocationCountryCode$kCGImagePropertyIPTCExtLocationCountryName$kCGImagePropertyIPTCExtLocationCreated$kCGImagePropertyIPTCExtLocationGPSAltitude$kCGImagePropertyIPTCExtLocationGPSLatitude$kCGImagePropertyIPTCExtLocationGPSLongitude$kCGImagePropertyIPTCExtLocationIdentifier$kCGImagePropertyIPTCExtLocationLocationId$kCGImagePropertyIPTCExtLocationLocationName$kCGImagePropertyIPTCExtLocationProvinceState$kCGImagePropertyIPTCExtLocationShown$kCGImagePropertyIPTCExtLocationSublocation$kCGImagePropertyIPTCExtLocationWorldRegion$kCGImagePropertyIPTCExtMaxAvailHeight$kCGImagePropertyIPTCExtMaxAvailWidth$kCGImagePropertyIPTCExtModelAge$kCGImagePropertyIPTCExtOrganisationInImageCode$kCGImagePropertyIPTCExtOrganisationInImageName$kCGImagePropertyIPTCExtPersonHeard$kCGImagePropertyIPTCExtPersonHeardIdentifier$kCGImagePropertyIPTCExtPersonHeardName$kCGImagePropertyIPTCExtPersonInImage$kCGImagePropertyIPTCExtPersonInImageCharacteristic$kCGImagePropertyIPTCExtPersonInImageCvTermCvId$kCGImagePropertyIPTCExtPersonInImageCvTermId$kCGImagePropertyIPTCExtPersonInImageCvTermName$kCGImagePropertyIPTCExtPersonInImageCvTermRefinedAbout$kCGImagePropertyIPTCExtPersonInImageDescription$kCGImagePropertyIPTCExtPersonInImageId$kCGImagePropertyIPTCExtPersonInImageName$kCGImagePropertyIPTCExtPersonInImageWDetails$kCGImagePropertyIPTCExtProductInImage$kCGImagePropertyIPTCExtProductInImageDescription$kCGImagePropertyIPTCExtProductInImageGTIN$kCGImagePropertyIPTCExtProductInImageName$kCGImagePropertyIPTCExtPublicationEvent$kCGImagePropertyIPTCExtPublicationEventDate$kCGImagePropertyIPTCExtPublicationEventIdentifier$kCGImagePropertyIPTCExtPublicationEventName$kCGImagePropertyIPTCExtRating$kCGImagePropertyIPTCExtRatingRatingRegion$kCGImagePropertyIPTCExtRatingRegionCity$kCGImagePropertyIPTCExtRatingRegionCountryCode$kCGImagePropertyIPTCExtRatingRegionCountryName$kCGImagePropertyIPTCExtRatingRegionGPSAltitude$kCGImagePropertyIPTCExtRatingRegionGPSLatitude$kCGImagePropertyIPTCExtRatingRegionGPSLongitude$kCGImagePropertyIPTCExtRatingRegionIdentifier$kCGImagePropertyIPTCExtRatingRegionLocationId$kCGImagePropertyIPTCExtRatingRegionLocationName$kCGImagePropertyIPTCExtRatingRegionProvinceState$kCGImagePropertyIPTCExtRatingRegionSublocation$kCGImagePropertyIPTCExtRatingRegionWorldRegion$kCGImagePropertyIPTCExtRatingScaleMaxValue$kCGImagePropertyIPTCExtRatingScaleMinValue$kCGImagePropertyIPTCExtRatingSourceLink$kCGImagePropertyIPTCExtRatingValue$kCGImagePropertyIPTCExtRatingValueLogoLink$kCGImagePropertyIPTCExtRegistryEntryRole$kCGImagePropertyIPTCExtRegistryID$kCGImagePropertyIPTCExtRegistryItemID$kCGImagePropertyIPTCExtRegistryOrganisationID$kCGImagePropertyIPTCExtReleaseReady$kCGImagePropertyIPTCExtSeason$kCGImagePropertyIPTCExtSeasonIdentifier$kCGImagePropertyIPTCExtSeasonName$kCGImagePropertyIPTCExtSeasonNumber$kCGImagePropertyIPTCExtSeries$kCGImagePropertyIPTCExtSeriesIdentifier$kCGImagePropertyIPTCExtSeriesName$kCGImagePropertyIPTCExtShownEvent$kCGImagePropertyIPTCExtShownEventIdentifier$kCGImagePropertyIPTCExtShownEventName$kCGImagePropertyIPTCExtStorylineIdentifier$kCGImagePropertyIPTCExtStreamReady$kCGImagePropertyIPTCExtStylePeriod$kCGImagePropertyIPTCExtSupplyChainSource$kCGImagePropertyIPTCExtSupplyChainSourceIdentifier$kCGImagePropertyIPTCExtSupplyChainSourceName$kCGImagePropertyIPTCExtTemporalCoverage$kCGImagePropertyIPTCExtTemporalCoverageFrom$kCGImagePropertyIPTCExtTemporalCoverageTo$kCGImagePropertyIPTCExtTranscript$kCGImagePropertyIPTCExtTranscriptLink$kCGImagePropertyIPTCExtTranscriptLinkLink$kCGImagePropertyIPTCExtTranscriptLinkLinkQualifier$kCGImagePropertyIPTCExtVideoBitrate$kCGImagePropertyIPTCExtVideoBitrateMode$kCGImagePropertyIPTCExtVideoDisplayAspectRatio$kCGImagePropertyIPTCExtVideoEncodingProfile$kCGImagePropertyIPTCExtVideoShotType$kCGImagePropertyIPTCExtVideoShotTypeIdentifier$kCGImagePropertyIPTCExtVideoShotTypeName$kCGImagePropertyIPTCExtVideoStreamsCount$kCGImagePropertyIPTCExtVisualColor$kCGImagePropertyIPTCExtWorkflowTag$kCGImagePropertyIPTCExtWorkflowTagCvId$kCGImagePropertyIPTCExtWorkflowTagCvTermId$kCGImagePropertyIPTCExtWorkflowTagCvTermName$kCGImagePropertyIPTCExtWorkflowTagCvTermRefinedAbout$kCGImagePropertyIPTCFixtureIdentifier$kCGImagePropertyIPTCHeadline$kCGImagePropertyIPTCImageOrientation$kCGImagePropertyIPTCImageType$kCGImagePropertyIPTCKeywords$kCGImagePropertyIPTCLanguageIdentifier$kCGImagePropertyIPTCObjectAttributeReference$kCGImagePropertyIPTCObjectCycle$kCGImagePropertyIPTCObjectName$kCGImagePropertyIPTCObjectTypeReference$kCGImagePropertyIPTCOriginalTransmissionReference$kCGImagePropertyIPTCOriginatingProgram$kCGImagePropertyIPTCProgramVersion$kCGImagePropertyIPTCProvinceState$kCGImagePropertyIPTCReferenceDate$kCGImagePropertyIPTCReferenceNumber$kCGImagePropertyIPTCReferenceService$kCGImagePropertyIPTCReleaseDate$kCGImagePropertyIPTCReleaseTime$kCGImagePropertyIPTCRightsUsageTerms$kCGImagePropertyIPTCScene$kCGImagePropertyIPTCSource$kCGImagePropertyIPTCSpecialInstructions$kCGImagePropertyIPTCStarRating$kCGImagePropertyIPTCSubLocation$kCGImagePropertyIPTCSubjectReference$kCGImagePropertyIPTCSupplementalCategory$kCGImagePropertyIPTCTimeCreated$kCGImagePropertyIPTCUrgency$kCGImagePropertyIPTCWriterEditor$kCGImagePropertyImageCount$kCGImagePropertyImageIndex$kCGImagePropertyImages$kCGImagePropertyIsFloat$kCGImagePropertyIsIndexed$kCGImagePropertyIsSticker$kCGImagePropertyJFIFDensityUnit$kCGImagePropertyJFIFDictionary$kCGImagePropertyJFIFIsProgressive$kCGImagePropertyJFIFVersion$kCGImagePropertyJFIFXDensity$kCGImagePropertyJFIFYDensity$kCGImagePropertyMakerAppleDictionary$kCGImagePropertyMakerCanonAspectRatioInfo$kCGImagePropertyMakerCanonCameraSerialNumber$kCGImagePropertyMakerCanonContinuousDrive$kCGImagePropertyMakerCanonDictionary$kCGImagePropertyMakerCanonFirmware$kCGImagePropertyMakerCanonFlashExposureComp$kCGImagePropertyMakerCanonImageSerialNumber$kCGImagePropertyMakerCanonLensModel$kCGImagePropertyMakerCanonOwnerName$kCGImagePropertyMakerFujiDictionary$kCGImagePropertyMakerMinoltaDictionary$kCGImagePropertyMakerNikonCameraSerialNumber$kCGImagePropertyMakerNikonColorMode$kCGImagePropertyMakerNikonDictionary$kCGImagePropertyMakerNikonDigitalZoom$kCGImagePropertyMakerNikonFlashExposureComp$kCGImagePropertyMakerNikonFlashSetting$kCGImagePropertyMakerNikonFocusDistance$kCGImagePropertyMakerNikonFocusMode$kCGImagePropertyMakerNikonISOSelection$kCGImagePropertyMakerNikonISOSetting$kCGImagePropertyMakerNikonImageAdjustment$kCGImagePropertyMakerNikonLensAdapter$kCGImagePropertyMakerNikonLensInfo$kCGImagePropertyMakerNikonLensType$kCGImagePropertyMakerNikonQuality$kCGImagePropertyMakerNikonSharpenMode$kCGImagePropertyMakerNikonShootingMode$kCGImagePropertyMakerNikonShutterCount$kCGImagePropertyMakerNikonWhiteBalanceMode$kCGImagePropertyMakerOlympusDictionary$kCGImagePropertyMakerPentaxDictionary$kCGImagePropertyNamedColorSpace$kCGImagePropertyOpenEXRAspectRatio$kCGImagePropertyOpenEXRDictionary$kCGImagePropertyOrientation$kCGImagePropertyPNGAuthor$kCGImagePropertyPNGChromaticities$kCGImagePropertyPNGComment$kCGImagePropertyPNGCompressionFilter$kCGImagePropertyPNGCopyright$kCGImagePropertyPNGCreationTime$kCGImagePropertyPNGDescription$kCGImagePropertyPNGDictionary$kCGImagePropertyPNGDisclaimer$kCGImagePropertyPNGGamma$kCGImagePropertyPNGInterlaceType$kCGImagePropertyPNGModificationTime$kCGImagePropertyPNGSoftware$kCGImagePropertyPNGSource$kCGImagePropertyPNGTitle$kCGImagePropertyPNGTransparency$kCGImagePropertyPNGWarning$kCGImagePropertyPNGXPixelsPerMeter$kCGImagePropertyPNGYPixelsPerMeter$kCGImagePropertyPNGsRGBIntent$kCGImagePropertyPixelFormat$kCGImagePropertyPixelHeight$kCGImagePropertyPixelWidth$kCGImagePropertyPrimaryImage$kCGImagePropertyProfileName$kCGImagePropertyRawDictionary$kCGImagePropertyTGACompression$kCGImagePropertyTGADictionary$kCGImagePropertyTIFFArtist$kCGImagePropertyTIFFCompression$kCGImagePropertyTIFFCopyright$kCGImagePropertyTIFFDateTime$kCGImagePropertyTIFFDictionary$kCGImagePropertyTIFFDocumentName$kCGImagePropertyTIFFHostComputer$kCGImagePropertyTIFFImageDescription$kCGImagePropertyTIFFMake$kCGImagePropertyTIFFModel$kCGImagePropertyTIFFOrientation$kCGImagePropertyTIFFPhotometricInterpretation$kCGImagePropertyTIFFPrimaryChromaticities$kCGImagePropertyTIFFResolutionUnit$kCGImagePropertyTIFFSoftware$kCGImagePropertyTIFFTileLength$kCGImagePropertyTIFFTileWidth$kCGImagePropertyTIFFTransferFunction$kCGImagePropertyTIFFWhitePoint$kCGImagePropertyTIFFXResolution$kCGImagePropertyTIFFYResolution$kCGImagePropertyThumbnailImages$kCGImagePropertyWebPCanvasPixelHeight$kCGImagePropertyWebPCanvasPixelWidth$kCGImagePropertyWebPDelayTime$kCGImagePropertyWebPDictionary$kCGImagePropertyWebPFrameInfoArray$kCGImagePropertyWebPLoopCount$kCGImagePropertyWebPUnclampedDelayTime$kCGImagePropertyWidth$kCGImageSourceCreateThumbnailFromImageAlways$kCGImageSourceCreateThumbnailFromImageIfAbsent$kCGImageSourceCreateThumbnailWithTransform$kCGImageSourceShouldAllowFloat$kCGImageSourceShouldCache$kCGImageSourceShouldCacheImmediately$kCGImageSourceSubsampleFactor$kCGImageSourceThumbnailMaxPixelSize$kCGImageSourceTypeIdentifierHint$"""
enums = """$IIO_HAS_IOSURFACE@1$IMAGEIO_PNG_ALL_FILTERS@248$IMAGEIO_PNG_FILTER_AVG@64$IMAGEIO_PNG_FILTER_NONE@8$IMAGEIO_PNG_FILTER_PAETH@128$IMAGEIO_PNG_FILTER_SUB@16$IMAGEIO_PNG_FILTER_UP@32$IMAGEIO_PNG_NO_FILTERS@0$kCGImageAnimationStatus_AllocationFailure@-22144$kCGImageAnimationStatus_CorruptInputImage@-22141$kCGImageAnimationStatus_IncompleteInputImage@-22143$kCGImageAnimationStatus_ParameterError@-22140$kCGImageAnimationStatus_UnsupportedFormat@-22142$kCGImageMetadataErrorBadArgument@2$kCGImageMetadataErrorConflictingArguments@3$kCGImageMetadataErrorPrefixConflict@4$kCGImageMetadataErrorUnknown@0$kCGImageMetadataErrorUnsupportedFormat@1$kCGImageMetadataTypeAlternateArray@4$kCGImageMetadataTypeAlternateText@5$kCGImageMetadataTypeArrayOrdered@3$kCGImageMetadataTypeArrayUnordered@2$kCGImageMetadataTypeDefault@0$kCGImageMetadataTypeInvalid@-1$kCGImageMetadataTypeString@1$kCGImageMetadataTypeStructure@6$kCGImagePropertyOrientationDown@3$kCGImagePropertyOrientationDownMirrored@4$kCGImagePropertyOrientationLeft@8$kCGImagePropertyOrientationLeftMirrored@5$kCGImagePropertyOrientationRight@6$kCGImagePropertyOrientationRightMirrored@7$kCGImagePropertyOrientationUp@1$kCGImagePropertyOrientationUpMirrored@2$kCGImageStatusComplete@0$kCGImageStatusIncomplete@-1$kCGImageStatusInvalidData@-4$kCGImageStatusReadingHeader@-2$kCGImageStatusUnexpectedEOF@-5$kCGImageStatusUnknownType@-3$kCGImageTGACompressionNone@0$kCGImageTGACompressionRLE@1$"""
misc.update({})
functions = {
    "CGImageMetadataSetValueMatchingImageProperty": (
        b"B^{CGImageMetadata=}^{__CFString=}^{__CFString=}@",
    ),
    "CGImageMetadataCreateFromXMPData": (
        b"^{CGImageMetadata=}^{__CFData=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceGetCount": (b"Q^{CGImageSource=}",),
    "CGImageSourceCreateWithData": (
        b"^{CGImageSource=}^{__CFData=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceCopyTypeIdentifiers": (
        b"^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataCopyTagWithPath": (
        b"^{CGImageMetadataTag=}^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataGetTypeID": (b"Q",),
    "CGImageDestinationAddAuxiliaryDataInfo": (
        b"v^{CGImageDestination=}^{__CFString=}^{__CFDictionary=}",
    ),
    "CGImageMetadataTagGetType": (b"i^{CGImageMetadataTag=}",),
    "CGImageSourceGetStatus": (b"i^{CGImageSource=}",),
    "CGImageMetadataCreateXMPData": (
        b"^{__CFData=}^{CGImageMetadata=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceCreateImageAtIndex": (
        b"^{CGImage=}^{CGImageSource=}Q^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataTagCopyNamespace": (
        b"^{__CFString=}^{CGImageMetadataTag=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceCopyMetadataAtIndex": (
        b"^{CGImageMetadata=}^{CGImageSource=}Q^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageDestinationCreateWithURL": (
        b"^{CGImageDestination=}^{__CFURL=}^{__CFString=}Q^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceRemoveCacheAtIndex": (b"v^{CGImageSource=}Q",),
    "CGImageSourceCreateThumbnailAtIndex": (
        b"^{CGImage=}^{CGImageSource=}Q^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceCreateIncremental": (
        b"^{CGImageSource=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceCopyPropertiesAtIndex": (
        b"^{__CFDictionary=}^{CGImageSource=}Q^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceUpdateData": (b"v^{CGImageSource=}^{__CFData=}B",),
    "CGImageDestinationSetProperties": (b"v^{CGImageDestination=}^{__CFDictionary=}",),
    "CGImageMetadataSetTagWithPath": (
        b"B^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}^{CGImageMetadataTag=}",
    ),
    "CGAnimateImageAtURLWithBlock": (
        b"i^{__CFURL=}^{__CFDictionary=}@?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "l"},
                            2: {"type": "@"},
                            3: {"type": "o^B"},
                        },
                    }
                }
            }
        },
    ),
    "CGImageDestinationCreateWithDataConsumer": (
        b"^{CGImageDestination=}^{CGDataConsumer=}^{__CFString=}Q^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageDestinationCopyTypeIdentifiers": (
        b"^{__CFArray=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageDestinationCreateWithData": (
        b"^{CGImageDestination=}^{__CFData=}^{__CFString=}Q^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceCopyAuxiliaryDataInfoAtIndex": (
        b"^{__CFDictionary=}^{CGImageSource=}Q^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGAnimateImageDataWithBlock": (
        b"i^{__CFData=}^{__CFDictionary=}@?",
        "",
        {
            "arguments": {
                2: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "l"},
                            2: {"type": "@"},
                            3: {"type": "o^B"},
                        },
                    }
                }
            }
        },
    ),
    "CGImageSourceGetTypeID": (b"Q",),
    "CGImageDestinationAddImageAndMetadata": (
        b"v^{CGImageDestination=}^{CGImage=}^{CGImageMetadata=}^{__CFDictionary=}",
    ),
    "CGImageMetadataTagCreate": (
        b"^{CGImageMetadataTag=}^{__CFString=}^{__CFString=}^{__CFString=}i@",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageDestinationCopyImageSource": (
        b"B^{CGImageDestination=}^{CGImageSource=}^{__CFDictionary=}^^{__CFError=}",
        "",
        {
            "retval": {"already_cfretained": True},
            "arguments": {
                3: {
                    "already_cfretained": True,
                    "type_modifier": "o",
                    "null_accepted": True,
                }
            },
        },
    ),
    "CGImageSourceUpdateDataProvider": (b"v^{CGImageSource=}^{CGDataProvider=}B",),
    "CGImageDestinationAddImage": (
        b"v^{CGImageDestination=}^{CGImage=}^{__CFDictionary=}",
    ),
    "CGImageMetadataRemoveTagWithPath": (
        b"B^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}",
    ),
    "CGImageSourceGetStatusAtIndex": (b"i^{CGImageSource=}Q",),
    "CGImageSourceCreateWithURL": (
        b"^{CGImageSource=}^{__CFURL=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataTagCopyValue": (
        b"@^{CGImageMetadataTag=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataCopyTags": (
        b"^{__CFArray=}^{CGImageMetadata=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataCopyStringValueWithPath": (
        b"^{__CFString=}^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceGetType": (b"^{__CFString=}^{CGImageSource=}",),
    "CGImageDestinationAddImageFromSource": (
        b"v^{CGImageDestination=}^{CGImageSource=}Q^{__CFDictionary=}",
    ),
    "CGImageDestinationGetTypeID": (b"Q",),
    "CGImageDestinationFinalize": (b"B^{CGImageDestination=}",),
    "CGImageSourceGetPrimaryImageIndex": (b"Q^{CGImageSource=}",),
    "CGImageSourceCopyProperties": (
        b"^{__CFDictionary=}^{CGImageSource=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataTagGetTypeID": (b"Q",),
    "CGImageMetadataSetValueWithPath": (
        b"B^{CGImageMetadata=}^{CGImageMetadataTag=}^{__CFString=}@",
    ),
    "CGImageMetadataCopyTagMatchingImageProperty": (
        b"^{CGImageMetadataTag=}^{CGImageMetadata=}^{__CFString=}^{__CFString=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataRegisterNamespaceForPrefix": (
        b"B^{CGImageMetadata=}^{__CFString=}^{__CFString=}^^{__CFError=}",
        "",
        {
            "arguments": {
                3: {
                    "already_cfretained": True,
                    "type_modifier": "o",
                    "null_accepted": True,
                }
            }
        },
    ),
    "CGImageMetadataTagCopyPrefix": (
        b"^{__CFString=}^{CGImageMetadataTag=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataTagCopyName": (
        b"^{__CFString=}^{CGImageMetadataTag=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataEnumerateTagsUsingBlock": (
        b"v^{CGImageMetadata=}^{__CFString=}^{__CFDictionary=}@?",
        "",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"B"},
                        "arguments": {
                            0: {"type": "^v"},
                            1: {"type": "@"},
                            2: {"type": "@"},
                        },
                    }
                }
            }
        },
    ),
    "CGImageMetadataCreateMutable": (
        b"^{CGImageMetadata=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageSourceCreateWithDataProvider": (
        b"^{CGImageSource=}^{CGDataProvider=}^{__CFDictionary=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataTagCopyQualifiers": (
        b"^{__CFArray=}^{CGImageMetadataTag=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
    "CGImageMetadataCreateMutableCopy": (
        b"^{CGImageMetadata=}^{CGImageMetadata=}",
        "",
        {"retval": {"already_cfretained": True}},
    ),
}
aliases = {
    "IMAGEIO_AVAILABLE_STARTING": "__OSX_AVAILABLE_STARTING",
    "IMAGEIO_AVAILABLE_BUT_DEPRECATED": "__OSX_AVAILABLE_BUT_DEPRECATED",
    "_iio_Nullable": "_Nullable",
    "_iio_Nonnull": "_Nonnull",
}
cftypes = [
    ("CGImageSourceRef", b"^{CGImageSource=}", "CGImageSourceGetTypeID", None),
    (
        "CGImageDestinationRef",
        b"^{CGImageDestination=}",
        "CGImageDestinationGetTypeID",
        None,
    ),
    (
        "CGImageMetadataTagRef",
        b"^{CGImageMetadataTag=}",
        "CGImageMetadataTagGetTypeID",
        None,
    ),
    ("CGImageMetadataRef", b"^{CGImageMetadata=}", "CGImageMetadataGetTypeID", None),
]
expressions = {}

# END OF FILE
