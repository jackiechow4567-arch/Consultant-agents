import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));

/** Agent SDK project root (`physician-pubs-bot/`). */
export function projectRoot(): string {
  return path.resolve(here, "../..");
}
