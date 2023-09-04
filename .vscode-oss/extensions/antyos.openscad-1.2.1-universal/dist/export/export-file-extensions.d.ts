/**-----------------------------------------------------------------------------
 * Export File Extensions
 *
 * Contains types and objects relating to exportable file types
 *----------------------------------------------------------------------------*/
/** List of all file exportable extensions */
export declare const ExportFileExtensionList: readonly ["stl", "off", "amf", "3mf", "csg", "dxf", "svg", "png", "echo", "ast", "term", "nef3", "nefdbg"];
/** Avaiable file extensions for export */
export type ExportFileExtension = typeof ExportFileExtensionList[number];
/** File types used in save dialogue */
export declare const ExportExtensionsForSave: {
    STL: string[];
    OFF: string[];
    AMF: string[];
    '3MF': string[];
    CSG: string[];
    DXF: string[];
    SVG: string[];
    PNG: string[];
    'Echo file output': string[];
    AST: string[];
    TERM: string[];
    NEF3: string[];
    NEFDBG: string[];
};
