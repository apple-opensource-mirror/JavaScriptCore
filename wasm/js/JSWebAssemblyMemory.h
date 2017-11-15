/*
 * Copyright (C) 2016-2017 Apple Inc. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY APPLE INC. ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE INC. OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#pragma once

#if ENABLE(WEBASSEMBLY)

#include "JSDestructibleObject.h"
#include "JSObject.h"
#include "WasmMemory.h"
#include <wtf/RefPtr.h>

namespace JSC {

class ArrayBuffer;
class JSArrayBuffer;

class JSWebAssemblyMemory : public JSDestructibleObject {
public:
    typedef JSDestructibleObject Base;

    static JSWebAssemblyMemory* create(ExecState*, VM&, Structure*, Ref<Wasm::Memory>&&);
    static Structure* createStructure(VM&, JSGlobalObject*, JSValue);

    DECLARE_EXPORT_INFO;

    Wasm::Memory& memory() { return m_memory.get(); }
    JSArrayBuffer* buffer(VM& vm, JSGlobalObject*);
    Wasm::PageCount grow(VM&, ExecState*, uint32_t delta, bool shouldThrowExceptionsOnFailure);

    static ptrdiff_t offsetOfMemory() { return OBJECT_OFFSETOF(JSWebAssemblyMemory, m_memoryBase); }
    static ptrdiff_t offsetOfSize() { return OBJECT_OFFSETOF(JSWebAssemblyMemory, m_memorySize); }

private:
    JSWebAssemblyMemory(VM&, Structure*, Ref<Wasm::Memory>&&);
    void finishCreation(VM&);
    static void destroy(JSCell*);
    static void visitChildren(JSCell*, SlotVisitor&);

    void* m_memoryBase;
    size_t m_memorySize;
    Ref<Wasm::Memory> m_memory;
    WriteBarrier<JSArrayBuffer> m_bufferWrapper;
    RefPtr<ArrayBuffer> m_buffer;
};

} // namespace JSC

#endif // ENABLE(WEBASSEMBLY)
