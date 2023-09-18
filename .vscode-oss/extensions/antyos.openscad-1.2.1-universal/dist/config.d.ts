/**-----------------------------------------------------------------------------
 * Config
 *
 * Interface containing all configurations that are used by Typescript parts of extension
 *----------------------------------------------------------------------------*/
/** Extension config values */
export interface ScadConfig {
    openscadPath?: string;
    launchArgs?: string[];
    maxInstances?: number;
    showKillMessage?: boolean;
    preferredExportFileExtension?: string;
    autoNamingFormat?: string;
    useAutoNamingExport?: boolean;
    useAutoNamingInSaveDialogues?: boolean;
    displayInStatusBar?: string;
    colorScheme?: string;
    openToSide?: string;
}