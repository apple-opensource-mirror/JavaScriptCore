{
    'variables': {
        'project_dir': ['.'],
        # These headers are part of JavaScriptCore's public API in the Apple Mac build.
        'javascriptcore_publicheader_files': [
            'API/JSBase.h',
            'API/JSContextRef.h',
            'API/JSObjectRef.h',
            'API/JSStringRef.h',
            'API/JSStringRefCF.h',
            'API/JSValueRef.h',
            'API/JavaScript.h',
            'API/JavaScriptCore.h',
            'API/WebKitAvailability.h',
        ],
        # These headers are part of JavaScriptCore's private API in the Apple Mac build.
        'javascriptcore_privateheader_files': [
            'API/APICast.h',
            'API/APIShims.h',
            'API/JSBasePrivate.h',
            'API/JSContextRefPrivate.h',
            'API/JSObjectRefPrivate.h',
            'API/JSProfilerPrivate.h',
            'API/JSRetainPtr.h',
            'API/JSWeakObjectMapRefInternal.h',
            'API/JSWeakObjectMapRefPrivate.h',
            'API/OpaqueJSString.h',
            'assembler/MacroAssemblerCodeRef.h',
            'bytecode/Opcode.h',
            'heap/ConservativeRoots.h',
            'heap/Handle.h',
            'heap/HandleHeap.h',
            'heap/SlotVisitor.h',
            'heap/HandleStack.h',
            'heap/HandleTypes.h',
            'heap/Heap.h',
            'heap/Local.h',
            'heap/LocalScope.h',
            'heap/Strong.h',
            'heap/Weak.h',
            'config.h',
            'debugger/Debugger.h',
            'debugger/DebuggerActivation.h',
            'debugger/DebuggerCallFrame.h',
            'interpreter/CallFrame.h',
            'interpreter/Interpreter.h',
            'interpreter/Register.h',
            'interpreter/RegisterFile.h',
            'jit/ExecutableAllocator.h',
            'jit/JITCode.h',
            'jit/JITStubs.h',
            'jit/ThunkGenerators.h',
            'parser/ResultType.h',
            'parser/SourceCode.h',
            'parser/SourceProvider.h',
            'parser/SourceProviderCache.h',
            'profiler/CallIdentifier.h',
            'profiler/Profile.h',
            'profiler/ProfileNode.h',
            'profiler/Profiler.h',
            'runtime/ArgList.h',
            'runtime/ArrayPrototype.h',
            'runtime/BooleanObject.h',
            'runtime/CachedTranscendentalFunction.h',
            'runtime/CallData.h',
            'runtime/ClassInfo.h',
            'runtime/CommonIdentifiers.h',
            'runtime/Completion.h',
            'runtime/ConstructData.h',
            'runtime/DateInstance.h',
            'runtime/DateInstanceCache.h',
            'runtime/Error.h',
            'runtime/ExceptionHelpers.h',
            'runtime/FunctionConstructor.h',
            'runtime/FunctionPrototype.h',
            'runtime/GCActivityCallback.h',
            'runtime/Identifier.h',
            'runtime/InitializeThreading.h',
            'runtime/InternalFunction.h',
            'runtime/JSAPIValueWrapper.h',
            'runtime/JSArray.h',
            'runtime/JSByteArray.h',
            'runtime/JSCell.h',
            'runtime/JSFunction.h',
            'runtime/JSGlobalData.h',
            'runtime/JSGlobalObject.h',
            'runtime/JSLock.h',
            'runtime/JSObject.h',
            'runtime/JSObjectWithGlobalObject.h',
            'runtime/JSString.h',
            'runtime/JSType.h',
            'runtime/JSTypeInfo.h',
            'runtime/JSValue.h',
            'runtime/JSValueInlineMethods.h',
            'runtime/JSVariableObject.h',
            'runtime/JSWrapperObject.h',
            'runtime/Lookup.h',
            'runtime/MathObject.h',
            'runtime/MemoryStatistics.h',
            'runtime/NumberObject.h',
            'runtime/NumberPrototype.h',
            'runtime/NumericStrings.h',
            'runtime/ObjectPrototype.h',
            'runtime/Operations.h',
            'runtime/PropertyDescriptor.h',
            'runtime/PropertyMapHashTable.h',
            'runtime/PropertyNameArray.h',
            'runtime/PropertySlot.h',
            'runtime/Protect.h',
            'runtime/PutPropertySlot.h',
            'runtime/RegExp.h',
            'runtime/RegExpKey.h',
            'runtime/RegExpCache.h',
            'runtime/RegExpObject.h',
            'runtime/RopeImpl.h',
            'runtime/ScopeChain.h',
            'runtime/SmallStrings.h',
            'runtime/StringObject.h',
            'runtime/StringObjectThatMasqueradesAsUndefined.h',
            'runtime/StringPrototype.h',
            'runtime/Structure.h',
            'runtime/StructureChain.h',
            'runtime/StructureTransitionTable.h',
            'runtime/SymbolTable.h',
            'runtime/Terminator.h',
            'runtime/TimeoutChecker.h',
            'runtime/UString.h',
            'runtime/UStringBuilder.h',
            'runtime/WeakGCMap.h',
            'runtime/WeakRandom.h',
            'runtime/WriteBarrier.h',
            'wtf/ASCIICType.h',
            'wtf/AVLTree.h',
            'wtf/Alignment.h',
            'wtf/AlwaysInline.h',
            'wtf/Assertions.h',
            'wtf/Atomics.h',
            'wtf/Bitmap.h',
            'wtf/BlockStack.h',
            'wtf/BloomFilter.h',
            'wtf/BumpPointerAllocator.h',
            'wtf/ByteArray.h',
            'wtf/Complex.h',
            'wtf/CrossThreadRefCounted.h',
            'wtf/CryptographicallyRandomNumber.h',
            'wtf/CurrentTime.h',
            'wtf/DateMath.h',
            'wtf/DecimalNumber.h',
            'wtf/Decoder.h',
            'wtf/Deque.h',
            'wtf/DisallowCType.h',
            'wtf/DoublyLinkedList.h',
            'wtf/Encoder.h',
            'wtf/FastAllocBase.h',
            'wtf/FastMalloc.h',
            'wtf/FixedArray.h',
            'wtf/Forward.h',
            'wtf/GetPtr.h',
            'wtf/HashCountedSet.h',
            'wtf/HashFunctions.h',
            'wtf/HashIterators.h',
            'wtf/HashMap.h',
            'wtf/HashSet.h',
            'wtf/HashTable.h',
            'wtf/HashTraits.h',
            'wtf/HexNumber.h',
            'wtf/ListHashSet.h',
            'wtf/ListRefPtr.h',
            'wtf/Locker.h',
            'wtf/MD5.h',
            'wtf/MainThread.h',
            'wtf/MathExtras.h',
            'wtf/MessageQueue.h',
            'wtf/NonCopyingSort.h',
            'wtf/Noncopyable.h',
            'wtf/NotFound.h',
            'wtf/NullPtr.h',
            'wtf/OSAllocator.h',
            'wtf/OwnArrayPtr.h',
            'wtf/OwnFastMallocPtr.h',
            'wtf/OwnPtr.h',
            'wtf/OwnPtrCommon.h',
            'wtf/PageAllocation.h',
            'wtf/PageAllocationAligned.h',
            'wtf/PageBlock.h',
            'wtf/PageReservation.h',
            'wtf/PassOwnArrayPtr.h',
            'wtf/PassOwnPtr.h',
            'wtf/PassRefPtr.h',
            'wtf/PassTraits.h',
            'wtf/Platform.h',
            'wtf/PossiblyNull.h',
            'wtf/RandomNumber.h',
            'wtf/RefCounted.h',
            'wtf/RefCountedLeakCounter.h',
            'wtf/RefPtr.h',
            'wtf/RefPtrHashMap.h',
            'wtf/RetainPtr.h',
            'wtf/SentinelLinkedList.h',
            'wtf/SinglyLinkedList.h',
            'wtf/StackBounds.h',
            'wtf/StaticConstructors.h',
            'wtf/StdLibExtras.h',
            'wtf/StringExtras.h',
            'wtf/StringHasher.h',
            'wtf/ThreadSafeRefCounted.h',
            'wtf/ThreadSpecific.h',
            'wtf/Threading.h',
            'wtf/ThreadingPrimitives.h',
            'wtf/TypeTraits.h',
            'wtf/UnusedParam.h',
            'wtf/VMTags.h',
            'wtf/ValueCheck.h',
            'wtf/Vector.h',
            'wtf/VectorTraits.h',
            'wtf/WTFThreadData.h',
            'wtf/dtoa.h',
            'wtf/text/AtomicString.h',
            'wtf/text/AtomicStringHash.h',
            'wtf/text/AtomicStringImpl.h',
            'wtf/text/CString.h',
            'wtf/text/StringBuffer.h',
            'wtf/text/StringBuilder.h',
            'wtf/text/StringConcatenate.h',
            'wtf/text/StringHash.h',
            'wtf/text/StringImpl.h',
            'wtf/text/StringImplBase.h',
            'wtf/text/StringOperators.h',
            'wtf/text/TextPosition.h',
            'wtf/text/WTFString.h',
            'wtf/unicode/CharacterNames.h',
            'wtf/unicode/Collator.h',
            'wtf/unicode/UTF8.h',
            'wtf/unicode/Unicode.h',
            'wtf/unicode/icu/UnicodeIcu.h',
            'yarr/Yarr.h',
            'yarr/YarrInterpreter.h',
            'yarr/YarrPattern.h',
        ],
        'javascriptcore_files': [
            'API/APIShims.h',
            'API/JSBase.cpp',
            'API/JSCallbackConstructor.cpp',
            'API/JSCallbackConstructor.h',
            'API/JSCallbackFunction.cpp',
            'API/JSCallbackFunction.h',
            'API/JSCallbackObject.cpp',
            'API/JSCallbackObject.h',
            'API/JSCallbackObjectFunctions.h',
            'API/JSClassRef.cpp',
            'API/JSClassRef.h',
            'API/JSContextRef.cpp',
            'API/JSObjectRef.cpp',
            'API/JSProfilerPrivate.cpp',
            'API/JSStringRef.cpp',
            'API/JSStringRefBSTR.cpp',
            'API/JSStringRefBSTR.h',
            'API/JSStringRefCF.cpp',
            'API/JSValueRef.cpp',
            'API/JSWeakObjectMapRefPrivate.cpp',
            'API/OpaqueJSString.cpp',
            'AllInOneFile.cpp',
            'ForwardingHeaders/JavaScriptCore/APICast.h',
            'ForwardingHeaders/JavaScriptCore/APIShims.h',
            'ForwardingHeaders/JavaScriptCore/JSBase.h',
            'ForwardingHeaders/JavaScriptCore/JSContextRef.h',
            'ForwardingHeaders/JavaScriptCore/JSObjectRef.h',
            'ForwardingHeaders/JavaScriptCore/JSRetainPtr.h',
            'ForwardingHeaders/JavaScriptCore/JSStringRef.h',
            'ForwardingHeaders/JavaScriptCore/JSStringRefCF.h',
            'ForwardingHeaders/JavaScriptCore/JSValueRef.h',
            'ForwardingHeaders/JavaScriptCore/JavaScript.h',
            'ForwardingHeaders/JavaScriptCore/JavaScriptCore.h',
            'ForwardingHeaders/JavaScriptCore/OpaqueJSString.h',
            'ForwardingHeaders/JavaScriptCore/WebKitAvailability.h',
            'JavaScriptCorePrefix.h',
            'assembler/ARMAssembler.cpp',
            'assembler/ARMAssembler.h',
            'assembler/ARMv7Assembler.cpp',
            'assembler/ARMv7Assembler.h',
            'assembler/AbstractMacroAssembler.h',
            'assembler/AssemblerBuffer.h',
            'assembler/AssemblerBufferWithConstantPool.h',
            'assembler/CodeLocation.h',
            'assembler/LinkBuffer.h',
            'assembler/MIPSAssembler.h',
            'assembler/MacroAssembler.h',
            'assembler/MacroAssemblerARM.cpp',
            'assembler/MacroAssemblerARM.h',
            'assembler/MacroAssemblerARMv7.h',
            'assembler/MacroAssemblerMIPS.h',
            'assembler/MacroAssemblerX86.h',
            'assembler/MacroAssemblerX86Common.h',
            'assembler/MacroAssemblerX86_64.h',
            'assembler/RepatchBuffer.h',
            'assembler/X86Assembler.h',
            'bytecode/CodeBlock.cpp',
            'bytecode/CodeBlock.h',
            'bytecode/EvalCodeCache.h',
            'bytecode/Instruction.h',
            'bytecode/JumpTable.cpp',
            'bytecode/JumpTable.h',
            'bytecode/Opcode.cpp',
            'bytecode/SamplingTool.cpp',
            'bytecode/SamplingTool.h',
            'bytecode/StructureStubInfo.cpp',
            'bytecode/StructureStubInfo.h',
            'bytecompiler/BytecodeGenerator.cpp',
            'bytecompiler/BytecodeGenerator.h',
            'bytecompiler/Label.h',
            'bytecompiler/LabelScope.h',
            'bytecompiler/NodesCodegen.cpp',
            'bytecompiler/RegisterID.h',
            'heap/ConservativeRoots.cpp',
            'heap/HandleHeap.cpp',
            'heap/HandleStack.cpp',
            'heap/Heap.cpp',
            'heap/MachineStackMarker.cpp',
            'heap/MachineStackMarker.h',
            'heap/MarkStack.cpp',
            'heap/MarkStack.h',
            'heap/HeapRootVisitor.h',
            'heap/MarkedBlock.cpp',
            'heap/MarkedBlock.h',
            'heap/MarkedBlockSet.h',
            'heap/TinyBloomFilter.h',
            'heap/NewSpace.cpp',
            'heap/NewSpace.h',
            'heap/OldSpace.cpp',
            'heap/OldSpace.h',
            'debugger/Debugger.cpp',
            'debugger/DebuggerActivation.cpp',
            'debugger/DebuggerCallFrame.cpp',
            'dfg/DFGAliasTracker.h',
            'dfg/DFGByteCodeParser.cpp',
            'dfg/DFGByteCodeParser.h',
            'dfg/DFGGenerationInfo.h',
            'dfg/DFGGraph.cpp',
            'dfg/DFGGraph.h',
            'dfg/DFGJITCodeGenerator.cpp',
            'dfg/DFGJITCodeGenerator.h',
            'dfg/DFGJITCompiler.cpp',
            'dfg/DFGJITCompiler.h',
            'dfg/DFGNode.h',
            'dfg/DFGNonSpeculativeJIT.cpp',
            'dfg/DFGNonSpeculativeJIT.h',
            'dfg/DFGOperations.cpp',
            'dfg/DFGOperations.h',
            'dfg/DFGRegisterBank.h',
            'dfg/DFGScoreBoard.h',
            'dfg/DFGSpeculativeJIT.cpp',
            'dfg/DFGSpeculativeJIT.h',
            'icu/unicode/parseerr.h',
            'icu/unicode/platform.h',
            'icu/unicode/putil.h',
            'icu/unicode/uchar.h',
            'icu/unicode/ucnv.h',
            'icu/unicode/ucnv_err.h',
            'icu/unicode/ucol.h',
            'icu/unicode/uconfig.h',
            'icu/unicode/uenum.h',
            'icu/unicode/uiter.h',
            'icu/unicode/uloc.h',
            'icu/unicode/umachine.h',
            'icu/unicode/unorm.h',
            'icu/unicode/urename.h',
            'icu/unicode/uscript.h',
            'icu/unicode/uset.h',
            'icu/unicode/ustring.h',
            'icu/unicode/utf.h',
            'icu/unicode/utf16.h',
            'icu/unicode/utf8.h',
            'icu/unicode/utf_old.h',
            'icu/unicode/utypes.h',
            'icu/unicode/uversion.h',
            'interpreter/CachedCall.h',
            'interpreter/CallFrame.cpp',
            'interpreter/CallFrameClosure.h',
            'interpreter/Interpreter.cpp',
            'interpreter/RegisterFile.cpp',
            'jit/ExecutableAllocator.cpp',
            'jit/ExecutableAllocatorFixedVMPool.cpp',
            'jit/JIT.cpp',
            'jit/JIT.h',
            'jit/JITArithmetic.cpp',
            'jit/JITArithmetic32_64.cpp',
            'jit/JITCall.cpp',
            'jit/JITCall32_64.cpp',
            'jit/JITInlineMethods.h',
            'jit/JITOpcodes.cpp',
            'jit/JITOpcodes32_64.cpp',
            'jit/JITPropertyAccess.cpp',
            'jit/JITPropertyAccess32_64.cpp',
            'jit/JITStubCall.h',
            'jit/JITStubs.cpp',
            'jit/JSInterfaceJIT.h',
            'jit/SpecializedThunkJIT.h',
            'jit/ThunkGenerators.cpp',
            'os-win32/WinMain.cpp',
            'os-win32/inttypes.h',
            'os-win32/stdbool.h',
            'os-win32/stdint.h',
            'parser/ASTBuilder.h',
            'parser/JSParser.cpp',
            'parser/JSParser.h',
            'parser/Lexer.cpp',
            'parser/Lexer.h',
            'parser/NodeConstructors.h',
            'parser/NodeInfo.h',
            'parser/Nodes.cpp',
            'parser/Nodes.h',
            'parser/Parser.cpp',
            'parser/Parser.h',
            'parser/ParserArena.cpp',
            'parser/ParserArena.h',
            'parser/SourceProviderCache.cpp',
            'parser/SourceProviderCacheItem.h',
            'parser/SyntaxChecker.h',
            'profiler/Profile.cpp',
            'profiler/ProfileGenerator.cpp',
            'profiler/ProfileGenerator.h',
            'profiler/ProfileNode.cpp',
            'profiler/Profiler.cpp',
            'profiler/ProfilerServer.h',
            'profiler/ProfilerServer.mm',
            'qt/api/qscriptconverter_p.h',
            'qt/api/qscriptengine.cpp',
            'qt/api/qscriptengine.h',
            'qt/api/qscriptengine_p.cpp',
            'qt/api/qscriptengine_p.h',
            'qt/api/qscriptfunction.cpp',
            'qt/api/qscriptfunction_p.h',
            'qt/api/qscriptoriginalglobalobject_p.h',
            'qt/api/qscriptprogram.cpp',
            'qt/api/qscriptprogram.h',
            'qt/api/qscriptprogram_p.h',
            'qt/api/qscriptstring.cpp',
            'qt/api/qscriptstring.h',
            'qt/api/qscriptstring_p.h',
            'qt/api/qscriptsyntaxcheckresult.cpp',
            'qt/api/qscriptsyntaxcheckresult.h',
            'qt/api/qscriptsyntaxcheckresult_p.h',
            'qt/api/qscriptvalue.cpp',
            'qt/api/qscriptvalue.h',
            'qt/api/qscriptvalue_p.h',
            'qt/api/qscriptvalueiterator.cpp',
            'qt/api/qscriptvalueiterator.h',
            'qt/api/qscriptvalueiterator_p.h',
            'qt/api/qtscriptglobal.h',
            'qt/benchmarks/qscriptengine/tst_qscriptengine.cpp',
            'qt/benchmarks/qscriptvalue/tst_qscriptvalue.cpp',
            'qt/tests/qscriptengine/tst_qscriptengine.cpp',
            'qt/tests/qscriptstring/tst_qscriptstring.cpp',
            'qt/tests/qscriptvalue/tst_qscriptvalue.cpp',
            'qt/tests/qscriptvalue/tst_qscriptvalue.h',
            'qt/tests/qscriptvalue/tst_qscriptvalue_generated_comparison.cpp',
            'qt/tests/qscriptvalue/tst_qscriptvalue_generated_init.cpp',
            'qt/tests/qscriptvalue/tst_qscriptvalue_generated_istype.cpp',
            'qt/tests/qscriptvalue/tst_qscriptvalue_generated_totype.cpp',
            'qt/tests/qscriptvalueiterator/tst_qscriptvalueiterator.cpp',
            'runtime/ArgList.cpp',
            'runtime/Arguments.cpp',
            'runtime/Arguments.h',
            'runtime/ArrayConstructor.cpp',
            'runtime/ArrayConstructor.h',
            'runtime/ArrayPrototype.cpp',
            'runtime/BatchedTransitionOptimizer.h',
            'runtime/BooleanConstructor.cpp',
            'runtime/BooleanConstructor.h',
            'runtime/BooleanObject.cpp',
            'runtime/BooleanPrototype.cpp',
            'runtime/BooleanPrototype.h',
            'runtime/CallData.cpp',
            'runtime/CommonIdentifiers.cpp',
            'runtime/Completion.cpp',
            'runtime/ConstructData.cpp',
            'runtime/DateConstructor.cpp',
            'runtime/DateConstructor.h',
            'runtime/DateConversion.cpp',
            'runtime/DateConversion.h',
            'runtime/DateInstance.cpp',
            'runtime/DatePrototype.cpp',
            'runtime/DatePrototype.h',
            'runtime/Error.cpp',
            'runtime/ErrorConstructor.cpp',
            'runtime/ErrorConstructor.h',
            'runtime/ErrorInstance.cpp',
            'runtime/ErrorInstance.h',
            'runtime/ErrorPrototype.cpp',
            'runtime/ErrorPrototype.h',
            'runtime/ExceptionHelpers.cpp',
            'runtime/Executable.cpp',
            'runtime/Executable.h',
            'runtime/FunctionConstructor.cpp',
            'runtime/FunctionPrototype.cpp',
            'runtime/GCActivityCallback.cpp',
            'runtime/GCActivityCallbackCF.cpp',
            'runtime/GetterSetter.cpp',
            'runtime/GetterSetter.h',
            'runtime/Identifier.cpp',
            'runtime/InitializeThreading.cpp',
            'runtime/InternalFunction.cpp',
            'runtime/JSAPIValueWrapper.cpp',
            'runtime/JSActivation.cpp',
            'runtime/JSActivation.h',
            'runtime/JSArray.cpp',
            'runtime/JSByteArray.cpp',
            'runtime/JSCell.cpp',
            'runtime/JSFunction.cpp',
            'runtime/JSGlobalData.cpp',
            'runtime/JSGlobalObject.cpp',
            'runtime/JSGlobalObjectFunctions.cpp',
            'runtime/JSGlobalObjectFunctions.h',
            'runtime/JSLock.cpp',
            'runtime/JSNotAnObject.cpp',
            'runtime/JSNotAnObject.h',
            'runtime/JSONObject.cpp',
            'runtime/JSONObject.h',
            'runtime/JSObject.cpp',
            'runtime/JSObjectWithGlobalObject.cpp',
            'runtime/JSPropertyNameIterator.cpp',
            'runtime/JSPropertyNameIterator.h',
            'runtime/JSStaticScopeObject.cpp',
            'runtime/JSStaticScopeObject.h',
            'runtime/JSString.cpp',
            'runtime/JSStringBuilder.h',
            'runtime/JSValue.cpp',
            'runtime/JSVariableObject.cpp',
            'runtime/JSWrapperObject.cpp',
            'runtime/LiteralParser.cpp',
            'runtime/LiteralParser.h',
            'runtime/Lookup.cpp',
            'runtime/MathObject.cpp',
            'runtime/MemoryStatistics.cpp',
            'runtime/NativeErrorConstructor.cpp',
            'runtime/NativeErrorConstructor.h',
            'runtime/NativeErrorPrototype.cpp',
            'runtime/NativeErrorPrototype.h',
            'runtime/NumberConstructor.cpp',
            'runtime/NumberConstructor.h',
            'runtime/NumberObject.cpp',
            'runtime/NumberPrototype.cpp',
            'runtime/ObjectConstructor.cpp',
            'runtime/ObjectConstructor.h',
            'runtime/ObjectPrototype.cpp',
            'runtime/Operations.cpp',
            'runtime/PropertyDescriptor.cpp',
            'runtime/PropertyNameArray.cpp',
            'runtime/PropertySlot.cpp',
            'runtime/RegExp.cpp',
            'runtime/RegExpCache.cpp',
            'runtime/RegExpConstructor.cpp',
            'runtime/RegExpConstructor.h',
            'runtime/RegExpMatchesArray.h',
            'runtime/RegExpObject.cpp',
            'runtime/RegExpPrototype.cpp',
            'runtime/RegExpPrototype.h',
            'runtime/RopeImpl.cpp',
            'runtime/ScopeChain.cpp',
            'runtime/ScopeChainMark.h',
            'runtime/SmallStrings.cpp',
            'runtime/StrictEvalActivation.cpp',
            'runtime/StrictEvalActivation.h',
            'runtime/StringConstructor.cpp',
            'runtime/StringConstructor.h',
            'runtime/StringObject.cpp',
            'runtime/StringPrototype.cpp',
            'runtime/StringRecursionChecker.cpp',
            'runtime/StringRecursionChecker.h',
            'runtime/Structure.cpp',
            'runtime/StructureChain.cpp',
            'runtime/TimeoutChecker.cpp',
            'runtime/Tracing.d',
            'runtime/Tracing.h',
            'runtime/UString.cpp',
            'runtime/UStringConcatenate.h',
            'wtf/Assertions.cpp',
            'wtf/ByteArray.cpp',
            'wtf/CryptographicallyRandomNumber.cpp',
            'wtf/CurrentTime.cpp',
            'wtf/DateMath.cpp',
            'wtf/DecimalNumber.cpp',
            'wtf/DynamicAnnotations.cpp',
            'wtf/DynamicAnnotations.h',
            'wtf/FastMalloc.cpp',
            'wtf/HashTable.cpp',
            'wtf/MD5.cpp',
            'wtf/MainThread.cpp',
            'wtf/MallocZoneSupport.h',
            'wtf/NullPtr.cpp',
            'wtf/OSAllocatorPosix.cpp',
            'wtf/OSAllocatorSymbian.cpp',
            'wtf/OSAllocatorWin.cpp',
            'wtf/OSRandomSource.cpp',
            'wtf/OSRandomSource.h',
            'wtf/PageAllocationAligned.cpp',
            'wtf/PageAllocatorSymbian.h',
            'wtf/PageBlock.cpp',
            'wtf/RandomNumber.cpp',
            'wtf/RandomNumberSeed.h',
            'wtf/RefCountedLeakCounter.cpp',
            'wtf/SHA1.cpp',
            'wtf/SHA1.h',
            'wtf/SegmentedVector.h',
            'wtf/SizeLimits.cpp',
            'wtf/StackBounds.cpp',
            'wtf/StringExtras.cpp',
            'wtf/TCPackedCache.h',
            'wtf/TCPageMap.h',
            'wtf/TCSpinLock.h',
            'wtf/TCSystemAlloc.cpp',
            'wtf/TCSystemAlloc.h',
            'wtf/ThreadFunctionInvocation.h',
            'wtf/ThreadIdentifierDataPthreads.cpp',
            'wtf/ThreadIdentifierDataPthreads.h',
            'wtf/ThreadSpecificWin.cpp',
            'wtf/Threading.cpp',
            'wtf/ThreadingNone.cpp',
            'wtf/ThreadingPthreads.cpp',
            'wtf/ThreadingWin.cpp',
            'wtf/TypeTraits.cpp',
            'wtf/WTFThreadData.cpp',
            'wtf/android/AndroidThreading.h',
            'wtf/android/MainThreadAndroid.cpp',
            'wtf/brew/MainThreadBrew.cpp',
            'wtf/brew/OwnPtrBrew.cpp',
            'wtf/brew/RefPtrBrew.h',
            'wtf/brew/ShellBrew.h',
            'wtf/brew/StringBrew.cpp',
            'wtf/brew/SystemMallocBrew.h',
            'wtf/chromium/ChromiumThreading.h',
            'wtf/chromium/MainThreadChromium.cpp',
            'wtf/dtoa.cpp',
            'wtf/efl/MainThreadEfl.cpp',
            'wtf/gobject/GOwnPtr.cpp',
            'wtf/gobject/GOwnPtr.h',
            'wtf/gobject/GRefPtr.cpp',
            'wtf/gobject/GRefPtr.h',
            'wtf/gobject/GTypedefs.h',
            'wtf/gtk/MainThreadGtk.cpp',
            'wtf/gtk/ThreadingGtk.cpp',
            'wtf/haiku/MainThreadHaiku.cpp',
            'wtf/haiku/StringHaiku.cpp',
            'wtf/mac/MainThreadMac.mm',
            'wtf/qt/MainThreadQt.cpp',
            'wtf/qt/StringQt.cpp',
            'wtf/qt/ThreadingQt.cpp',
            'wtf/text/AtomicString.cpp',
            'wtf/text/CString.cpp',
            'wtf/text/StringBuilder.cpp',
            'wtf/text/StringImpl.cpp',
            'wtf/text/StringStatics.cpp',
            'wtf/text/WTFString.cpp',
            'wtf/unicode/CollatorDefault.cpp',
            'wtf/unicode/ScriptCodesFromICU.h',
            'wtf/unicode/UTF8.cpp',
            'wtf/unicode/UnicodeMacrosFromICU.h',
            'wtf/unicode/brew/UnicodeBrew.cpp',
            'wtf/unicode/brew/UnicodeBrew.h',
            'wtf/unicode/glib/UnicodeGLib.cpp',
            'wtf/unicode/glib/UnicodeGLib.h',
            'wtf/unicode/icu/CollatorICU.cpp',
            'wtf/unicode/qt4/UnicodeQt4.h',
            'wtf/unicode/wince/UnicodeWinCE.cpp',
            'wtf/unicode/wince/UnicodeWinCE.h',
            'wtf/win/MainThreadWin.cpp',
            'wtf/win/OwnPtrWin.cpp',
            'wtf/wince/FastMallocWinCE.h',
            'wtf/wince/MemoryManager.cpp',
            'wtf/wince/MemoryManager.h',
            'wtf/wx/MainThreadWx.cpp',
            'wtf/wx/StringWx.cpp',
            'yarr/YarrInterpreter.cpp',
            'yarr/YarrJIT.cpp',
            'yarr/YarrJIT.h',
            'yarr/YarrParser.h',
            'yarr/YarrPattern.cpp',
            'yarr/YarrSyntaxChecker.cpp',
            'yarr/YarrSyntaxChecker.h',
        ],
        'javascriptcore_derived_source_files': [
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/Lexer.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/RegExpJitTables.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/TracingDtrace.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/ArrayConstructor.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/ArrayPrototype.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/BooleanPrototype.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/DateConstructor.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/DatePrototype.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/ErrorPrototype.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/JSGlobalObject.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/JSONObject.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/MathObject.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/NumberConstructor.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/NumberPrototype.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/ObjectConstructor.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/ObjectPrototype.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/RegExpConstructor.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/RegExpObject.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/RegExpPrototype.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/StringConstructor.lut.h',
            '<(PRODUCT_DIR)/DerivedSources/JavaScriptCore/StringPrototype.lut.h',
        ],
        'minidom_files': [
            'API/tests/JSNode.c',
            'API/tests/JSNode.h',
            'API/tests/JSNodeList.c',
            'API/tests/JSNodeList.h',
            'API/tests/Node.c',
            'API/tests/Node.h',
            'API/tests/NodeList.c',
            'API/tests/NodeList.h',
            'API/tests/minidom.c',
        ],
        'minidom_support_files': [
            'API/tests/minidom.js',
        ],
        'testapi_files': [
            'API/tests/testapi.c',
        ],
        'testapi_support_files': [
            'API/tests/testapi.js',
        ],
        'jsc_files': [
            'jsc.cpp',
        ],
    }
}
