#!/usr/bin/env python3
"""Restore the original poster PPTX from lossless parts and verify SHA-256."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
manifest = json.loads((root / 'checksums.json').read_text())
relative = 'poster/poster_camera_ready_editable.pptx'
expected = next(item for item in manifest['original_files'] if item['path'] == relative)
target = root / relative
if target.exists():
    if hashlib.sha256(target.read_bytes()).hexdigest() != expected['sha256']:
        raise SystemExit(f'Refusing to overwrite a modified file: {target}')
else:
    temporary = target.with_suffix('.pptx.restoring')
    digest = hashlib.sha256()
    with temporary.open('xb') as output:
        for item in manifest['poster_parts']:
            data = (root / item['path']).read_bytes()
            if len(data) != item['size'] or hashlib.sha256(data).hexdigest() != item['sha256']:
                raise SystemExit(f'Part verification failed: {item["path"]}')
            output.write(data)
            digest.update(data)
    if temporary.stat().st_size != expected['size'] or digest.hexdigest() != expected['sha256']:
        raise SystemExit('Restored file verification failed')
    temporary.rename(target)
print(f'Verified: {target}')
