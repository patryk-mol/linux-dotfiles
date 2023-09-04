/**-----------------------------------------------------------------------------
 * openscad-exe
 *
 * Manages access to the Openscad executable file
 *----------------------------------------------------------------------------*/
export interface OpenscadExecutable {
    version: string;
    filePath: string;
    arguments_: string[];
}
/** Open an instance of OpenSCAD to preview a file */
export declare class OpenscadExecutableManager {
    private openscadExecutable?;
    private openscadPath?;
    private arguments_;
    private getOpenscadVersion;
    /** Set the path to `openscad.exe` on the system.
     *
     * Note: Must be called before opening children.
     */
    updateScadPath(newOpenscadPath?: string, newArguments?: string[]): Promise<void>;
    /** A valid openscad executable or undefined */
    get executable(): OpenscadExecutable | undefined;
    /** The current path the manager is looking for openscad at. Not guaranteed
     * to be valid. */
    getPath(): string;
}
