using System;
using System.Collections.Specialized;
using System.Runtime.InteropServices;
using System.Text;
using ESRI.ArcGIS.Carto;
using ESRI.ArcGIS.DataSourcesGDB;
using ESRI.ArcGIS.esriSystem;
using ESRI.ArcGIS.Geodatabase;
using ESRI.ArcGIS.Geometry;
using ESRI.ArcGIS.Server;
using ESRI.ArcGIS.SOESupport;


//TODO: sign the project (project properties > signing tab > sign the assembly)
//      this is strongly suggested if the dll will be registered using regasm.exe <your>.dll /codebase


namespace IndexMismatch
{
    [ComVisible(true)]
    [Guid("c2c633ee-d6e1-4202-86dc-9b5b72309f5b")]
    [ClassInterface(ClassInterfaceType.None)]
    [ServerObjectExtension(
        "", //use "MapServer" if SOE extends a Map service and "ImageServer" if it extends an Image service.
        AllCapabilities = "",
        DefaultCapabilities = "",
        Description = "",
        DisplayName = "IndexMismatch",
        Properties = "",
        SupportsREST = true,
        SupportsSOAP = false)]
    public class IndexMismatch : IServerObjectExtension, IObjectConstruct, IRESTRequestHandler
    {
        private readonly IRESTRequestHandler _reqHandler;
        private readonly string _soeName;

       
       private static byte[] ReproHandler(NameValueCollection boundVariables,
            JsonObject operationInput,
            string outputFormat,
            string requestProperties,
            out string responseProperties)
        {
            responseProperties = null;

            // connect to SDE
            var propertySet = new PropertySet();
            propertySet.SetProperty("SERVER", "");
            propertySet.SetProperty("INSTANCE", "");
            propertySet.SetProperty("DATABASE", "");
            propertySet.SetProperty("USER", "");
            propertySet.SetProperty("PASSWORD", "");
            propertySet.SetProperty("VERSION", "sde.DEFAULT");

            var workspaceFactory = new SdeWorkspaceFactory();
            var workspace = workspaceFactory.Open(propertySet, 0);

            var featureWorkspace = workspace as IRasterWorkspaceEx;

            // open the dem in an SDE Raster Dataset with a Raster Attribute Table
            // our raster table has the schema objectid, value, count, feet
            var featureClass = featureWorkspace.OpenRasterDataset("DEM_10Meter");

            var rasterLayer = new RasterLayer();
            rasterLayer.CreateFromDataset(featureClass);

            var table = rasterLayer as ITable;
            var identify = rasterLayer as IIdentify;

            // create a point that will intersect your raster
            IPoint point = null;

            var results = identify.Identify(point);
            var item = results.Element[0] as IRasterIdentifyObj2;

            // this will return 1 for value since object id is 0, count is 2 and feet is 3
            var valueIndex = table.FindField("VALUE");

            string property;
            string value;
            item.GetPropAndValues(valueIndex, out property, out value);

            // when using the index 1, the property will be object id and the value will be the object id
            // when querying for feet, the correct property and value are returned.
            
            // The correct way
            var item2 = item as IIdentifyObject;
            object props;
            object values;
            item2.PropertySet.GetAllProperties(out props, out values);

            return Encoding.UTF8.GetBytes(property + ": " + value);
        }

        #region cruft
 
        public IndexMismatch()
        {
            _soeName = GetType().Name;
            _reqHandler = new SoeRestImpl(_soeName, CreateRestSchema());
        }

        public void Construct(IPropertySet props)
        {
        }

        private RestResource CreateRestSchema()
        {
            var rootRes = new RestResource(_soeName, false, RootResHandler);

            var sampleOper = new RestOperation("reproduceBug",
                new string[0],
                new[] { "json" },
                ReproHandler);

            rootRes.operations.Add(sampleOper);

            return rootRes;
        }

        private static byte[] RootResHandler(NameValueCollection boundVariables, string outputFormat,
            string requestProperties, out string responseProperties)
        {
            responseProperties = null;
            return Encoding.UTF8.GetBytes("ok");
        }

        public void Init(IServerObjectHelper pSoh)
        {
        }

        public void Shutdown()
        {
        }


        public string GetSchema()
        {
            return _reqHandler.GetSchema();
        }

        public byte[] HandleRESTRequest(string capabilities, string resourceName, string operationName,
            string operationInput, string outputFormat, string requestProperties, out string responseProperties)
        {
            return _reqHandler.HandleRESTRequest(capabilities, resourceName, operationName, operationInput,
                outputFormat, requestProperties, out responseProperties);
        }

        #endregion
    }
}
