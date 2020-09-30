# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "BIG_INT_BASE_TYPE",
  66: "HEAP_NUMBER_TYPE",
  67: "ODDBALL_TYPE",
  68: "ABSTRACT_INTERNAL_CLASS_SUBCLASS1_TYPE",
  69: "ABSTRACT_INTERNAL_CLASS_SUBCLASS2_TYPE",
  70: "FOREIGN_TYPE",
  71: "WASM_TYPE_INFO_TYPE",
  72: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  73: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  74: "CALLABLE_TASK_TYPE",
  75: "CALLBACK_TASK_TYPE",
  76: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  77: "LOAD_HANDLER_TYPE",
  78: "STORE_HANDLER_TYPE",
  79: "FUNCTION_TEMPLATE_INFO_TYPE",
  80: "OBJECT_TEMPLATE_INFO_TYPE",
  81: "ACCESS_CHECK_INFO_TYPE",
  82: "ACCESSOR_INFO_TYPE",
  83: "ACCESSOR_PAIR_TYPE",
  84: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  85: "ALLOCATION_MEMENTO_TYPE",
  86: "ALLOCATION_SITE_TYPE",
  87: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  88: "ASM_WASM_DATA_TYPE",
  89: "ASYNC_GENERATOR_REQUEST_TYPE",
  90: "BREAK_POINT_TYPE",
  91: "BREAK_POINT_INFO_TYPE",
  92: "CACHED_TEMPLATE_OBJECT_TYPE",
  93: "CALL_HANDLER_INFO_TYPE",
  94: "CLASS_POSITIONS_TYPE",
  95: "DEBUG_INFO_TYPE",
  96: "ENUM_CACHE_TYPE",
  97: "FEEDBACK_CELL_TYPE",
  98: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  99: "INTERCEPTOR_INFO_TYPE",
  100: "INTERPRETER_DATA_TYPE",
  101: "PROMISE_CAPABILITY_TYPE",
  102: "PROMISE_REACTION_TYPE",
  103: "PROPERTY_DESCRIPTOR_OBJECT_TYPE",
  104: "PROTOTYPE_INFO_TYPE",
  105: "SCRIPT_TYPE",
  106: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  107: "STACK_FRAME_INFO_TYPE",
  108: "STACK_TRACE_FRAME_TYPE",
  109: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  110: "TUPLE2_TYPE",
  111: "WASM_CAPI_FUNCTION_DATA_TYPE",
  112: "WASM_EXCEPTION_TAG_TYPE",
  113: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  114: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  115: "WASM_JS_FUNCTION_DATA_TYPE",
  116: "WASM_VALUE_TYPE",
  117: "FIXED_ARRAY_TYPE",
  118: "HASH_TABLE_TYPE",
  119: "EPHEMERON_HASH_TABLE_TYPE",
  120: "GLOBAL_DICTIONARY_TYPE",
  121: "NAME_DICTIONARY_TYPE",
  122: "NUMBER_DICTIONARY_TYPE",
  123: "ORDERED_HASH_MAP_TYPE",
  124: "ORDERED_HASH_SET_TYPE",
  125: "ORDERED_NAME_DICTIONARY_TYPE",
  126: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  127: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  128: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  129: "SCOPE_INFO_TYPE",
  130: "SCRIPT_CONTEXT_TABLE_TYPE",
  131: "BYTE_ARRAY_TYPE",
  132: "BYTECODE_ARRAY_TYPE",
  133: "FIXED_DOUBLE_ARRAY_TYPE",
  134: "INTERNAL_CLASS_WITH_SMI_ELEMENTS_TYPE",
  135: "SLOPPY_ARGUMENTS_ELEMENTS_TYPE",
  136: "AWAIT_CONTEXT_TYPE",
  137: "BLOCK_CONTEXT_TYPE",
  138: "CATCH_CONTEXT_TYPE",
  139: "DEBUG_EVALUATE_CONTEXT_TYPE",
  140: "EVAL_CONTEXT_TYPE",
  141: "FUNCTION_CONTEXT_TYPE",
  142: "MODULE_CONTEXT_TYPE",
  143: "NATIVE_CONTEXT_TYPE",
  144: "SCRIPT_CONTEXT_TYPE",
  145: "WITH_CONTEXT_TYPE",
  146: "EXPORTED_SUB_CLASS_BASE_TYPE",
  147: "EXPORTED_SUB_CLASS_TYPE",
  148: "EXPORTED_SUB_CLASS2_TYPE",
  149: "SMALL_ORDERED_HASH_MAP_TYPE",
  150: "SMALL_ORDERED_HASH_SET_TYPE",
  151: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  152: "SOURCE_TEXT_MODULE_TYPE",
  153: "SYNTHETIC_MODULE_TYPE",
  154: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  155: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  156: "WEAK_FIXED_ARRAY_TYPE",
  157: "TRANSITION_ARRAY_TYPE",
  158: "CELL_TYPE",
  159: "CODE_TYPE",
  160: "CODE_DATA_CONTAINER_TYPE",
  161: "COVERAGE_INFO_TYPE",
  162: "DESCRIPTOR_ARRAY_TYPE",
  163: "EMBEDDER_DATA_ARRAY_TYPE",
  164: "FEEDBACK_METADATA_TYPE",
  165: "FEEDBACK_VECTOR_TYPE",
  166: "FILLER_TYPE",
  167: "FREE_SPACE_TYPE",
  168: "INTERNAL_CLASS_TYPE",
  169: "INTERNAL_CLASS_WITH_STRUCT_ELEMENTS_TYPE",
  170: "MAP_TYPE",
  171: "ON_HEAP_BASIC_BLOCK_PROFILER_DATA_TYPE",
  172: "PREPARSE_DATA_TYPE",
  173: "PROPERTY_ARRAY_TYPE",
  174: "PROPERTY_CELL_TYPE",
  175: "SHARED_FUNCTION_INFO_TYPE",
  176: "SMI_BOX_TYPE",
  177: "SMI_PAIR_TYPE",
  178: "SORT_STATE_TYPE",
  179: "WASM_ARRAY_TYPE",
  180: "WASM_STRUCT_TYPE",
  181: "WEAK_ARRAY_LIST_TYPE",
  182: "WEAK_CELL_TYPE",
  183: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  184: "JS_GLOBAL_OBJECT_TYPE",
  185: "JS_GLOBAL_PROXY_TYPE",
  186: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1042: "JS_MAP_KEY_ITERATOR_TYPE",
  1043: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1044: "JS_MAP_VALUE_ITERATOR_TYPE",
  1045: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1046: "JS_SET_VALUE_ITERATOR_TYPE",
  1047: "JS_GENERATOR_OBJECT_TYPE",
  1048: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1049: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1050: "JS_DATA_VIEW_TYPE",
  1051: "JS_TYPED_ARRAY_TYPE",
  1052: "JS_MAP_TYPE",
  1053: "JS_SET_TYPE",
  1054: "JS_WEAK_MAP_TYPE",
  1055: "JS_WEAK_SET_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_OBJECT_TYPE",
  1059: "JS_ARRAY_TYPE",
  1060: "JS_ARRAY_BUFFER_TYPE",
  1061: "JS_ARRAY_ITERATOR_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_COLLATOR_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_DATE_TIME_FORMAT_TYPE",
  1067: "JS_DISPLAY_NAMES_TYPE",
  1068: "JS_ERROR_TYPE",
  1069: "JS_FINALIZATION_REGISTRY_TYPE",
  1070: "JS_LIST_FORMAT_TYPE",
  1071: "JS_LOCALE_TYPE",
  1072: "JS_MESSAGE_OBJECT_TYPE",
  1073: "JS_NUMBER_FORMAT_TYPE",
  1074: "JS_PLURAL_RULES_TYPE",
  1075: "JS_PROMISE_TYPE",
  1076: "JS_REG_EXP_TYPE",
  1077: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  1078: "JS_RELATIVE_TIME_FORMAT_TYPE",
  1079: "JS_SEGMENT_ITERATOR_TYPE",
  1080: "JS_SEGMENTER_TYPE",
  1081: "JS_SEGMENTS_TYPE",
  1082: "JS_STRING_ITERATOR_TYPE",
  1083: "JS_V8_BREAK_ITERATOR_TYPE",
  1084: "JS_WEAK_REF_TYPE",
  1085: "WASM_EXCEPTION_OBJECT_TYPE",
  1086: "WASM_GLOBAL_OBJECT_TYPE",
  1087: "WASM_INSTANCE_OBJECT_TYPE",
  1088: "WASM_MEMORY_OBJECT_TYPE",
  1089: "WASM_MODULE_OBJECT_TYPE",
  1090: "WASM_TABLE_OBJECT_TYPE",
  1091: "JS_BOUND_FUNCTION_TYPE",
  1092: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x02115): (170, "MetaMap"),
  ("read_only_space", 0x0213d): (67, "NullMap"),
  ("read_only_space", 0x02165): (162, "DescriptorArrayMap"),
  ("read_only_space", 0x0218d): (156, "WeakFixedArrayMap"),
  ("read_only_space", 0x021cd): (96, "EnumCacheMap"),
  ("read_only_space", 0x02201): (117, "FixedArrayMap"),
  ("read_only_space", 0x0224d): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x02299): (167, "FreeSpaceMap"),
  ("read_only_space", 0x022c1): (166, "OnePointerFillerMap"),
  ("read_only_space", 0x022e9): (166, "TwoPointerFillerMap"),
  ("read_only_space", 0x02311): (67, "UninitializedMap"),
  ("read_only_space", 0x02389): (67, "UndefinedMap"),
  ("read_only_space", 0x023cd): (66, "HeapNumberMap"),
  ("read_only_space", 0x02401): (67, "TheHoleMap"),
  ("read_only_space", 0x02461): (67, "BooleanMap"),
  ("read_only_space", 0x02505): (131, "ByteArrayMap"),
  ("read_only_space", 0x0252d): (117, "FixedCOWArrayMap"),
  ("read_only_space", 0x02555): (118, "HashTableMap"),
  ("read_only_space", 0x0257d): (64, "SymbolMap"),
  ("read_only_space", 0x025a5): (40, "OneByteStringMap"),
  ("read_only_space", 0x025cd): (129, "ScopeInfoMap"),
  ("read_only_space", 0x025f5): (175, "SharedFunctionInfoMap"),
  ("read_only_space", 0x0261d): (159, "CodeMap"),
  ("read_only_space", 0x02645): (158, "CellMap"),
  ("read_only_space", 0x0266d): (174, "GlobalPropertyCellMap"),
  ("read_only_space", 0x02695): (70, "ForeignMap"),
  ("read_only_space", 0x026bd): (157, "TransitionArrayMap"),
  ("read_only_space", 0x026e5): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x0270d): (165, "FeedbackVectorMap"),
  ("read_only_space", 0x0273d): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x0279d): (67, "ExceptionMap"),
  ("read_only_space", 0x027f9): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x02861): (67, "OptimizedOutMap"),
  ("read_only_space", 0x028c1): (67, "StaleRegisterMap"),
  ("read_only_space", 0x02921): (130, "ScriptContextTableMap"),
  ("read_only_space", 0x02949): (127, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x02971): (164, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x02999): (117, "ArrayListMap"),
  ("read_only_space", 0x029c1): (65, "BigIntMap"),
  ("read_only_space", 0x029e9): (128, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x02a11): (132, "BytecodeArrayMap"),
  ("read_only_space", 0x02a39): (160, "CodeDataContainerMap"),
  ("read_only_space", 0x02a61): (161, "CoverageInfoMap"),
  ("read_only_space", 0x02a89): (133, "FixedDoubleArrayMap"),
  ("read_only_space", 0x02ab1): (120, "GlobalDictionaryMap"),
  ("read_only_space", 0x02ad9): (97, "ManyClosuresCellMap"),
  ("read_only_space", 0x02b01): (117, "ModuleInfoMap"),
  ("read_only_space", 0x02b29): (121, "NameDictionaryMap"),
  ("read_only_space", 0x02b51): (97, "NoClosuresCellMap"),
  ("read_only_space", 0x02b79): (122, "NumberDictionaryMap"),
  ("read_only_space", 0x02ba1): (97, "OneClosureCellMap"),
  ("read_only_space", 0x02bc9): (123, "OrderedHashMapMap"),
  ("read_only_space", 0x02bf1): (124, "OrderedHashSetMap"),
  ("read_only_space", 0x02c19): (125, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x02c41): (172, "PreparseDataMap"),
  ("read_only_space", 0x02c69): (173, "PropertyArrayMap"),
  ("read_only_space", 0x02c91): (93, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x02cb9): (93, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x02ce1): (93, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x02d09): (126, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x02d31): (149, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x02d59): (150, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x02d81): (151, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x02da9): (152, "SourceTextModuleMap"),
  ("read_only_space", 0x02dd1): (153, "SyntheticModuleMap"),
  ("read_only_space", 0x02df9): (155, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x02e21): (154, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x02e49): (71, "WasmTypeInfoMap"),
  ("read_only_space", 0x02e71): (181, "WeakArrayListMap"),
  ("read_only_space", 0x02e99): (119, "EphemeronHashTableMap"),
  ("read_only_space", 0x02ec1): (163, "EmbedderDataArrayMap"),
  ("read_only_space", 0x02ee9): (182, "WeakCellMap"),
  ("read_only_space", 0x02f11): (32, "StringMap"),
  ("read_only_space", 0x02f39): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x02f61): (33, "ConsStringMap"),
  ("read_only_space", 0x02f89): (37, "ThinStringMap"),
  ("read_only_space", 0x02fb1): (35, "SlicedStringMap"),
  ("read_only_space", 0x02fd9): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x03001): (34, "ExternalStringMap"),
  ("read_only_space", 0x03029): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x03051): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x03079): (0, "InternalizedStringMap"),
  ("read_only_space", 0x030a1): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x030c9): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x030f1): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x03119): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x03141): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x03169): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x03191): (67, "BasicBlockCountersMarkerMap"),
  ("read_only_space", 0x031d5): (87, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x032a5): (99, "InterceptorInfoMap"),
  ("read_only_space", 0x05399): (72, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x053c1): (73, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x053e9): (74, "CallableTaskMap"),
  ("read_only_space", 0x05411): (75, "CallbackTaskMap"),
  ("read_only_space", 0x05439): (76, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x05461): (79, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x05489): (80, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x054b1): (81, "AccessCheckInfoMap"),
  ("read_only_space", 0x054d9): (82, "AccessorInfoMap"),
  ("read_only_space", 0x05501): (83, "AccessorPairMap"),
  ("read_only_space", 0x05529): (84, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x05551): (85, "AllocationMementoMap"),
  ("read_only_space", 0x05579): (88, "AsmWasmDataMap"),
  ("read_only_space", 0x055a1): (89, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x055c9): (90, "BreakPointMap"),
  ("read_only_space", 0x055f1): (91, "BreakPointInfoMap"),
  ("read_only_space", 0x05619): (92, "CachedTemplateObjectMap"),
  ("read_only_space", 0x05641): (94, "ClassPositionsMap"),
  ("read_only_space", 0x05669): (95, "DebugInfoMap"),
  ("read_only_space", 0x05691): (98, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x056b9): (100, "InterpreterDataMap"),
  ("read_only_space", 0x056e1): (101, "PromiseCapabilityMap"),
  ("read_only_space", 0x05709): (102, "PromiseReactionMap"),
  ("read_only_space", 0x05731): (103, "PropertyDescriptorObjectMap"),
  ("read_only_space", 0x05759): (104, "PrototypeInfoMap"),
  ("read_only_space", 0x05781): (105, "ScriptMap"),
  ("read_only_space", 0x057a9): (106, "SourceTextModuleInfoEntryMap"),
  ("read_only_space", 0x057d1): (107, "StackFrameInfoMap"),
  ("read_only_space", 0x057f9): (108, "StackTraceFrameMap"),
  ("read_only_space", 0x05821): (109, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x05849): (110, "Tuple2Map"),
  ("read_only_space", 0x05871): (111, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x05899): (112, "WasmExceptionTagMap"),
  ("read_only_space", 0x058c1): (113, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x058e9): (114, "WasmIndirectFunctionTableMap"),
  ("read_only_space", 0x05911): (115, "WasmJSFunctionDataMap"),
  ("read_only_space", 0x05939): (116, "WasmValueMap"),
  ("read_only_space", 0x05961): (135, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x05989): (171, "OnHeapBasicBlockProfilerDataMap"),
  ("read_only_space", 0x059b1): (168, "InternalClassMap"),
  ("read_only_space", 0x059d9): (177, "SmiPairMap"),
  ("read_only_space", 0x05a01): (176, "SmiBoxMap"),
  ("read_only_space", 0x05a29): (146, "ExportedSubClassBaseMap"),
  ("read_only_space", 0x05a51): (147, "ExportedSubClassMap"),
  ("read_only_space", 0x05a79): (68, "AbstractInternalClassSubclass1Map"),
  ("read_only_space", 0x05aa1): (69, "AbstractInternalClassSubclass2Map"),
  ("read_only_space", 0x05ac9): (134, "InternalClassWithSmiElementsMap"),
  ("read_only_space", 0x05af1): (169, "InternalClassWithStructElementsMap"),
  ("read_only_space", 0x05b19): (148, "ExportedSubClass2Map"),
  ("read_only_space", 0x05b41): (178, "SortStateMap"),
  ("read_only_space", 0x05b69): (86, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x05b91): (86, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x05bb9): (77, "LoadHandler1Map"),
  ("read_only_space", 0x05be1): (77, "LoadHandler2Map"),
  ("read_only_space", 0x05c09): (77, "LoadHandler3Map"),
  ("read_only_space", 0x05c31): (78, "StoreHandler0Map"),
  ("read_only_space", 0x05c59): (78, "StoreHandler1Map"),
  ("read_only_space", 0x05c81): (78, "StoreHandler2Map"),
  ("read_only_space", 0x05ca9): (78, "StoreHandler3Map"),
  ("map_space", 0x02115): (1057, "ExternalMap"),
  ("map_space", 0x0213d): (1072, "JSMessageObjectMap"),
  ("map_space", 0x02165): (180, "WasmRttEqrefMap"),
  ("map_space", 0x0218d): (180, "WasmRttExternrefMap"),
  ("map_space", 0x021b5): (180, "WasmRttFuncrefMap"),
  ("map_space", 0x021dd): (180, "WasmRttI31refMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x021b5): "EmptyWeakFixedArray",
  ("read_only_space", 0x021bd): "EmptyDescriptorArray",
  ("read_only_space", 0x021f5): "EmptyEnumCache",
  ("read_only_space", 0x02229): "EmptyFixedArray",
  ("read_only_space", 0x02231): "NullValue",
  ("read_only_space", 0x02339): "UninitializedValue",
  ("read_only_space", 0x023b1): "UndefinedValue",
  ("read_only_space", 0x023f5): "NanValue",
  ("read_only_space", 0x02429): "TheHoleValue",
  ("read_only_space", 0x02455): "HoleNanValue",
  ("read_only_space", 0x02489): "TrueValue",
  ("read_only_space", 0x024c9): "FalseValue",
  ("read_only_space", 0x024f9): "empty_string",
  ("read_only_space", 0x02735): "EmptyScopeInfo",
  ("read_only_space", 0x02765): "ArgumentsMarker",
  ("read_only_space", 0x027c5): "Exception",
  ("read_only_space", 0x02821): "TerminationException",
  ("read_only_space", 0x02889): "OptimizedOut",
  ("read_only_space", 0x028e9): "StaleRegister",
  ("read_only_space", 0x031b9): "EmptyPropertyArray",
  ("read_only_space", 0x031c1): "EmptyByteArray",
  ("read_only_space", 0x031c9): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x031fd): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x03209): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x03211): "EmptySlowElementDictionary",
  ("read_only_space", 0x03235): "EmptyOrderedHashMap",
  ("read_only_space", 0x03249): "EmptyOrderedHashSet",
  ("read_only_space", 0x0325d): "EmptyFeedbackMetadata",
  ("read_only_space", 0x03269): "EmptyPropertyCell",
  ("read_only_space", 0x0327d): "EmptyPropertyDictionary",
  ("read_only_space", 0x032cd): "NoOpInterceptorInfo",
  ("read_only_space", 0x032f5): "EmptyWeakArrayList",
  ("read_only_space", 0x03301): "InfinityValue",
  ("read_only_space", 0x0330d): "MinusZeroValue",
  ("read_only_space", 0x03319): "MinusInfinityValue",
  ("read_only_space", 0x03325): "SelfReferenceMarker",
  ("read_only_space", 0x03365): "BasicBlockCountersMarker",
  ("read_only_space", 0x033a9): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x033b5): "TrampolineTrivialCodeDataContainer",
  ("read_only_space", 0x033c1): "TrampolinePromiseRejectionCodeDataContainer",
  ("read_only_space", 0x033cd): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x03405): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x0342d): "NativeScopeInfo",
  ("read_only_space", 0x03449): "HashSeed",
  ("old_space", 0x02115): "ArgumentsIteratorAccessor",
  ("old_space", 0x02159): "ArrayLengthAccessor",
  ("old_space", 0x0219d): "BoundFunctionLengthAccessor",
  ("old_space", 0x021e1): "BoundFunctionNameAccessor",
  ("old_space", 0x02225): "ErrorStackAccessor",
  ("old_space", 0x02269): "FunctionArgumentsAccessor",
  ("old_space", 0x022ad): "FunctionCallerAccessor",
  ("old_space", 0x022f1): "FunctionNameAccessor",
  ("old_space", 0x02335): "FunctionLengthAccessor",
  ("old_space", 0x02379): "FunctionPrototypeAccessor",
  ("old_space", 0x023bd): "RegExpResultIndicesAccessor",
  ("old_space", 0x02401): "StringLengthAccessor",
  ("old_space", 0x02445): "InvalidPrototypeValidityCell",
  ("old_space", 0x024cd): "EmptyScript",
  ("old_space", 0x0250d): "ManyClosuresCell",
  ("old_space", 0x02519): "ArrayConstructorProtector",
  ("old_space", 0x0252d): "NoElementsProtector",
  ("old_space", 0x02541): "IsConcatSpreadableProtector",
  ("old_space", 0x02555): "ArraySpeciesProtector",
  ("old_space", 0x02569): "TypedArraySpeciesProtector",
  ("old_space", 0x0257d): "PromiseSpeciesProtector",
  ("old_space", 0x02591): "RegExpSpeciesProtector",
  ("old_space", 0x025a5): "StringLengthProtector",
  ("old_space", 0x025b9): "ArrayIteratorProtector",
  ("old_space", 0x025cd): "ArrayBufferDetachingProtector",
  ("old_space", 0x025e1): "PromiseHookProtector",
  ("old_space", 0x025f5): "PromiseResolveProtector",
  ("old_space", 0x02609): "MapIteratorProtector",
  ("old_space", 0x0261d): "PromiseThenProtector",
  ("old_space", 0x02631): "SetIteratorProtector",
  ("old_space", 0x02645): "StringIteratorProtector",
  ("old_space", 0x02659): "SingleCharacterStringCache",
  ("old_space", 0x02a61): "StringSplitCache",
  ("old_space", 0x02e69): "RegExpMultipleCache",
  ("old_space", 0x03271): "BuiltinsConstantsTable",
  ("old_space", 0x0364d): "AsyncFunctionAwaitRejectSharedFun",
  ("old_space", 0x03675): "AsyncFunctionAwaitResolveSharedFun",
  ("old_space", 0x0369d): "AsyncGeneratorAwaitRejectSharedFun",
  ("old_space", 0x036c5): "AsyncGeneratorAwaitResolveSharedFun",
  ("old_space", 0x036ed): "AsyncGeneratorYieldResolveSharedFun",
  ("old_space", 0x03715): "AsyncGeneratorReturnResolveSharedFun",
  ("old_space", 0x0373d): "AsyncGeneratorReturnClosedRejectSharedFun",
  ("old_space", 0x03765): "AsyncGeneratorReturnClosedResolveSharedFun",
  ("old_space", 0x0378d): "AsyncIteratorValueUnwrapSharedFun",
  ("old_space", 0x037b5): "PromiseAllResolveElementSharedFun",
  ("old_space", 0x037dd): "PromiseAllSettledResolveElementSharedFun",
  ("old_space", 0x03805): "PromiseAllSettledRejectElementSharedFun",
  ("old_space", 0x0382d): "PromiseAnyRejectElementSharedFun",
  ("old_space", 0x03855): "PromiseCapabilityDefaultRejectSharedFun",
  ("old_space", 0x0387d): "PromiseCapabilityDefaultResolveSharedFun",
  ("old_space", 0x038a5): "PromiseCatchFinallySharedFun",
  ("old_space", 0x038cd): "PromiseGetCapabilitiesExecutorSharedFun",
  ("old_space", 0x038f5): "PromiseThenFinallySharedFun",
  ("old_space", 0x0391d): "PromiseThrowerFinallySharedFun",
  ("old_space", 0x03945): "PromiseValueThunkFinallySharedFun",
  ("old_space", 0x0396d): "ProxyRevokeSharedFun",
}

# Lower 32 bits of first page addresses for various heap spaces.
HEAP_FIRST_PAGES = {
  0x08100000: "old_space",
  0x08140000: "map_space",
  0x08040000: "read_only_space",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_DEBUG_BREAK",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
