# This file is generated by objective.metadata
#
# Last update: Tue Jul 30 22:52:46 2019

import objc, sys

if sys.maxsize > 2 ** 32:
    def sel32or64(a, b): return b
else:
    def sel32or64(a, b): return a
if sys.byteorder == 'little':
    def littleOrBig(a, b): return a
else:
    def littleOrBig(a, b): return b

misc = {
}
constants = '''$JSPropertyDescriptorConfigurableKey$JSPropertyDescriptorEnumerableKey$JSPropertyDescriptorGetKey$JSPropertyDescriptorSetKey$JSPropertyDescriptorValueKey$JSPropertyDescriptorWritableKey$'''
enums = '''$WEBKIT_VERSION_1_0@256$WEBKIT_VERSION_1_1@272$WEBKIT_VERSION_1_2@288$WEBKIT_VERSION_1_3@304$WEBKIT_VERSION_2_0@512$WEBKIT_VERSION_3_0@768$WEBKIT_VERSION_3_1@784$WEBKIT_VERSION_4_0@1024$WEBKIT_VERSION_LATEST@39321$kJSClassAttributeNoAutomaticPrototype@2$kJSClassAttributeNone@0$kJSPropertyAttributeDontDelete@8$kJSPropertyAttributeDontEnum@4$kJSPropertyAttributeNone@0$kJSPropertyAttributeReadOnly@2$kJSTypeBoolean@2$kJSTypeNull@1$kJSTypeNumber@3$kJSTypeObject@5$kJSTypeString@4$kJSTypeSymbol@6$kJSTypeUndefined@0$kJSTypedArrayTypeArrayBuffer@9$kJSTypedArrayTypeFloat32Array@7$kJSTypedArrayTypeFloat64Array@8$kJSTypedArrayTypeInt16Array@1$kJSTypedArrayTypeInt32Array@2$kJSTypedArrayTypeInt8Array@0$kJSTypedArrayTypeNone@10$kJSTypedArrayTypeUint16Array@5$kJSTypedArrayTypeUint32Array@6$kJSTypedArrayTypeUint8Array@3$kJSTypedArrayTypeUint8ClampedArray@4$'''
misc.update({'JSC_OBJC_API_ENABLED': sel32or64(0, 1)})
misc.update({})
functions={'JSObjectSetPropertyForKey': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}', '', {'arguments': {5: {'type_modifier': 'o'}}}), 'JSClassRetain': (b'^{OpaqueJSClass=}^{OpaqueJSClass=}',), 'JSValueCreateJSONString': (b'^{OpaqueJSString=}^{OpaqueJSContext=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectDeletePropertyForKey': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSValueGetTypedArrayType': (b'I^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {2: {'type_modifier': 'o'}}}), 'JSStringCreateWithCFString': (b'^{OpaqueJSString=}^{__CFString=}', '', {'retval': {'already_cfretained': True}}), 'JSValueToBoolean': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSStringCopyCFString': (b'^{__CFString=}^{__CFAllocator=}^{OpaqueJSString=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectMakeTypedArray': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}IL^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSValueMakeString': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSObjectGetArrayBufferBytesPtr': (b'^v^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'retval': {'c_array_of_variable_length': True}, 'arguments': {2: {'type_modifier': 'o'}}}), 'JSObjectGetTypedArrayByteOffset': (sel32or64(b'L^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'Q^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'type_modifier': 'o'}}}), 'JSValueMakeNumber': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}d',), 'JSObjectMakeError': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'JSValueProtect': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsDate': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectGetTypedArrayBytesPtr': (b'^v^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'retval': {'c_array_of_variable_length': True}, 'arguments': {2: {'type_modifier': 'o'}}}), 'JSValueToStringCopy': (b'^{OpaqueJSString=}^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSValueIsNumber': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectHasProperty': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}',), 'JSValueIsEqual': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSValueIsArray': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueToNumber': (b'd^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSObjectMakeDeferredPromise': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^^{OpaqueJSValue=}^^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {1: {'type_modifier': 'o'}, 2: {'type_modifier': 'o'}}}), 'JSObjectGetTypedArrayByteLength': (sel32or64(b'L^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'Q^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'type_modifier': 'o'}}}), 'JSValueUnprotect': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectSetPropertyAtIndex': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}I^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {4: {'type_modifier': 'o'}}}), 'JSObjectGetTypedArrayLength': (sel32or64(b'L^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'Q^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'type_modifier': 'o'}}}), 'JSObjectCallAsFunction': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {4: {'c_array_length_in_arg': 3, 'type_modifier': 'n'}, 5: {'type_modifier': 'o'}}}), 'JSPropertyNameArrayGetCount': (sel32or64(b'L^{OpaqueJSPropertyNameArray=}', b'Q^{OpaqueJSPropertyNameArray=}'),), 'JSStringGetLength': (sel32or64(b'L^{OpaqueJSString=}', b'Q^{OpaqueJSString=}'),), 'JSValueToObject': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSValueIsString': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectCopyPropertyNames': (b'^{OpaqueJSPropertyNameArray=}^{OpaqueJSContext=}^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}}), 'JSGlobalContextCopyName': (b'^{OpaqueJSString=}^{OpaqueJSContext=}', '', {'retval': {'already_cfretained': True}}), 'JSClassRelease': (b'v^{OpaqueJSClass=}',), 'JSValueMakeUndefined': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSObjectMakeArray': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'JSGlobalContextSetName': (b'v^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSStringGetMaximumUTF8CStringSize': (sel32or64(b'L^{OpaqueJSString=}', b'Q^{OpaqueJSString=}'),), 'JSStringCreateWithCharacters': (sel32or64(b'^{OpaqueJSString=}^TL', b'^{OpaqueJSString=}^TQ'), '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}}}), 'JSValueIsSymbol': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSObjectMakeTypedArrayWithArrayBufferAndOffset': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}I^{OpaqueJSValue=}LL^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}I^{OpaqueJSValue=}QQ^^{OpaqueJSValue=}'), '', {'arguments': {5: {'type_modifier': 'o'}}}), 'JSObjectCallAsConstructor': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {3: {'c_array_length_in_arg': 2, 'type_modifier': 'n'}, 4: {'type_modifier': 'o'}}}), 'JSObjectIsFunction': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsInstanceOfConstructor': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}',), 'JSCheckScriptSyntax': (b'B^{OpaqueJSContext=}^{OpaqueJSString=}^{OpaqueJSString=}i^^{OpaqueJSValue=}', '', {'arguments': {4: {'type_modifier': 'o'}}}), 'JSObjectIsConstructor': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSPropertyNameArrayRelease': (b'v^{OpaqueJSPropertyNameArray=}',), 'JSValueIsBoolean': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSContextGroupRetain': (b'^{OpaqueJSContextGroup=}^{OpaqueJSContextGroup=}',), 'JSGlobalContextRetain': (b'^{OpaqueJSContext=}^{OpaqueJSContext=}',), 'JSStringRelease': (b'v^{OpaqueJSString=}',), 'JSObjectMakeFunctionWithCallback': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}^?', '', {'arguments': {2: {'callable': {'retval': {'type': b'^{OpaqueJSValue=}'}, 'arguments': {0: {'type': b'^{OpaqueJSContext=}'}, 1: {'type': b'^{OpaqueJSValue=}'}, 2: {'type': b'^{OpaqueJSValue=}'}, 3: {'type': b'L'}, 4: {'type': b'^^{OpaqueJSValue=}', 'type_modifier': 'n', 'c_array_length_in_arg': 3}, 5: {'type': b'^^{OpaqueJSValue=}', 'type_modifier': 'o'}}}}}}), 'JSValueIsObject': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSStringGetUTF8CString': (sel32or64(b'L^{OpaqueJSString=}^tL', b'Q^{OpaqueJSString=}^tQ'), '', {'arguments': {1: {'c_array_length_in_result': True, 'type_modifier': 'o', 'c_array_length_in_arg': 2}}}), 'JSGlobalContextCreate': (b'^{OpaqueJSContext=}^{OpaqueJSClass=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectSetProperty': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}', '', {'arguments': {5: {'type_modifier': 'o'}}}), 'JSValueMakeBoolean': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}B',), 'JSGlobalContextRelease': (b'v^{OpaqueJSContext=}',), 'JSObjectMakeRegExp': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'JSStringIsEqualToUTF8CString': (b'B^{OpaqueJSString=}^t', '', {'arguments': {1: {'c_array_delimited_by_null': True, 'type_modifier': 'n'}}}), 'JSObjectGetProperty': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSObjectMakeArrayBufferWithBytesNoCopy': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}^vL^?^v^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}^vQ^?^v^^{OpaqueJSValue=}'), '', {'retval': {'already_cfretained': True}, 'arguments': {1: {'c_array_length_in_arg': 2, 'type_modifier': 'n'}, 3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'^v'}}}, 'callable_retained': True}, 5: {'type_modifier': 'o'}}}), 'JSValueIsNull': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSPropertyNameAccumulatorAddName': (b'v^{OpaqueJSPropertyNameAccumulator=}^{OpaqueJSString=}',), 'JSStringRetain': (b'^{OpaqueJSString=}^{OpaqueJSString=}',), 'JSObjectHasPropertyForKey': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSObjectMakeConstructor': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSClass=}^?', '', {'arguments': {2: {'callable': {'retval': {'type': b'^{OpaqueJSValue=}'}, 'arguments': {0: {'type': b'^{OpaqueJSContext=}'}, 1: {'type': b'^{OpaqueJSValue=}'}, 2: {'type': b'L'}, 3: {'type': b'^^{OpaqueJSValue=}', 'type_modifier': 'n', 'c_array_length_in_arg': 2}, 4: {'type': b'^^{OpaqueJSValue=}', 'type_modifier': 'o'}}}}}}), 'JSObjectSetPrivate': (b'B^{OpaqueJSValue=}^v',), 'JSObjectMakeTypedArrayWithBytesNoCopy': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}I^vL^?^v^^{OpaqueJSValue=}', '', {'retval': {'already_cfretained': True}, 'arguments': {2: {'c_array_length_in_arg': 3, 'type_modifier': 'n'}, 4: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'^v'}}}}, 6: {'type_modifier': 'o'}}}), 'JSValueMakeFromJSONString': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSEvaluateScript': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}^{OpaqueJSValue=}^{OpaqueJSString=}i^^{OpaqueJSValue=}', '', {'arguments': {5: {'type_modifier': 'o'}}}), 'JSContextGetGlobalContext': (b'^{OpaqueJSContext=}^{OpaqueJSContext=}',), 'JSStringCreateWithUTF8CString': (b'^{OpaqueJSString=}^t', '', {'retval': {'already_cfretained': True}, 'arguments': {0: {'c_array_delimited_by_null': True, 'type_modifier': 'n'}}}), 'JSObjectGetTypedArrayBuffer': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {2: {'type_modifier': 'o'}}}), 'JSObjectGetArrayBufferByteLength': (sel32or64(b'L^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'Q^{OpaqueJSContext=}^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'type_modifier': 'o'}}}), 'JSContextGetGlobalObject': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSPropertyNameArrayRetain': (b'^{OpaqueJSPropertyNameArray=}^{OpaqueJSPropertyNameArray=}',), 'JSObjectMake': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSClass=}^v',), 'JSObjectGetPrivate': (b'^v^{OpaqueJSValue=}',), 'JSValueIsUndefined': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSValueIsObjectOfClass': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSClass=}',), 'JSObjectGetPrototype': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}',), 'JSPropertyNameArrayGetNameAtIndex': (sel32or64(b'^{OpaqueJSString=}^{OpaqueJSPropertyNameArray=}L', b'^{OpaqueJSString=}^{OpaqueJSPropertyNameArray=}Q'),), 'JSValueMakeNull': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}',), 'JSContextGetGroup': (b'^{OpaqueJSContextGroup=}^{OpaqueJSContext=}',), 'JSContextGroupCreate': (b'^{OpaqueJSContextGroup=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectDeleteProperty': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSString=}^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSObjectGetPropertyForKey': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSObjectMakeFunction': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}I^^{OpaqueJSString=}^{OpaqueJSString=}^{OpaqueJSString=}i^^{OpaqueJSValue=}', '', {'arguments': {3: {'c_array_length_in_arg': 2, 'type_modifier': 'n'}, 7: {'type_modifier': 'o'}}}), 'JSObjectGetPropertyAtIndex': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSValue=}I^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSStringIsEqual': (b'B^{OpaqueJSString=}^{OpaqueJSString=}',), 'JSObjectSetPrototype': (b'v^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}',), 'JSContextGroupRelease': (b'v^{OpaqueJSContextGroup=}',), 'JSValueIsStrictEqual': (b'B^{OpaqueJSContext=}^{OpaqueJSValue=}^{OpaqueJSValue=}',), 'JSGlobalContextCreateInGroup': (b'^{OpaqueJSContext=}^{OpaqueJSContextGroup=}^{OpaqueJSClass=}', '', {'retval': {'already_cfretained': True}}), 'JSObjectMakeDate': (sel32or64(b'^{OpaqueJSValue=}^{OpaqueJSContext=}L^^{OpaqueJSValue=}^^{OpaqueJSValue=}', b'^{OpaqueJSValue=}^{OpaqueJSContext=}Q^^{OpaqueJSValue=}^^{OpaqueJSValue=}'), '', {'arguments': {2: {'c_array_length_in_arg': 1, 'type_modifier': 'n'}, 3: {'type_modifier': 'o'}}}), 'JSObjectMakeTypedArrayWithArrayBuffer': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}I^{OpaqueJSValue=}^^{OpaqueJSValue=}', '', {'arguments': {3: {'type_modifier': 'o'}}}), 'JSValueMakeSymbol': (b'^{OpaqueJSValue=}^{OpaqueJSContext=}^{OpaqueJSString=}',), 'JSGarbageCollect': (b'v^{OpaqueJSContext=}',), 'JSValueGetType': (b'I^{OpaqueJSContext=}^{OpaqueJSValue=}',)}
aliases = {'JSObjectRef': 'JSValueRef', 'JSGlobalContextRef': 'JSContextRef'}
misc.update({'JSValueRef': objc.createOpaquePointerType('JSValueRef', b'^{OpaqueJSValue=}'), 'JSStringRef': objc.createOpaquePointerType('JSStringRef', b'^{OpaqueJSString=}'), 'JSContextRef': objc.createOpaquePointerType('JSContextRef', b'^{OpaqueJSContext=}'), 'JSPropertyNameArrayRef': objc.createOpaquePointerType('JSPropertyNameArrayRef', b'^{OpaqueJSPropertyNameArray=}'), 'JSClassRef': objc.createOpaquePointerType('JSClassRef', b'^{OpaqueJSClass=}'), 'JSContextGroupRef': objc.createOpaquePointerType('JSContextGroupRef', b'^{OpaqueJSContextGroup=}'), 'JSPropertyNameAccumulatorRef': objc.createOpaquePointerType('JSPropertyNameAccumulatorRef', b'^{OpaqueJSPropertyNameAccumulator=}')})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b'JSContext', b'exceptionHandler', {'retval': {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}})
    r(b'JSContext', b'setExceptionHandler:', {'arguments': {2: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
    r(b'JSValue', b'deleteProperty:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'hasProperty:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isArray', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isBoolean', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isDate', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isEqualToObject:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isEqualWithTypeCoercionToObject:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isInstanceOf:', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isNull', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isNumber', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isObject', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isString', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'isSymbol', {'retval': {'type': b'Z'}})
    r(b'JSValue', b'isUndefined', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'toBool', {'retval': {'type': 'Z'}})
    r(b'JSValue', b'valueWithBool:inContext:', {'arguments': {2: {'type': b'Z'}}})
    r(b'JSValue', b'valueWithNewPromiseInContext:fromExecutor:', {'arguments': {3: {'callable': {'retval': {'type': b'v'}, 'arguments': {0: {'type': b'^v'}, 1: {'type': b'@'}, 2: {'type': b'@'}}}}}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
