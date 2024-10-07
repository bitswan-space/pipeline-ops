import asyncio
import os


async def git_pull(bitswan_dir: str) -> bool:
    abspath = os.path.abspath(bitswan_dir)

    await asyncio.create_subprocess_exec(
        "git", "config", "--global", "--add", "safe.directory", abspath
    )

    await asyncio.create_subprocess_exec(
        "git", "config", "pull.rebase", "false", cwd=bitswan_dir
    )

    pull_proc = await asyncio.create_subprocess_exec("git", "pull", cwd=bitswan_dir)
    await pull_proc.wait()

    if pull_proc.returncode:
        return False

    return True


async def wait_coroutine(*args, **kwargs) -> int:
    coro = await asyncio.create_subprocess_exec(*args, **kwargs)
    result = await coro.wait()
    return result
